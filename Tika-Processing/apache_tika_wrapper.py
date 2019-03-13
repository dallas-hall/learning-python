#!/usr/bin/python
# @author: dhall
# @date: 2018-2-22
# @version: 0.2


# @@@ Imports @@@
import argparse, re, os, subprocess


# @@@ Global Variables @@@
debugging = False
tika_path = '/path/to/apache_tika/'
tika_file = 'tika-app-1.17.jar'
tika_threads = 8
tika_output_format = 'x'
script_path = os.getcwd() + '/'
output_path = script_path + 'output/'
final_output = []
final_file = 'load_data.csv'


# @@@ Functions @@@
# ### Check Path Exists ###
def check_path_exists(path):
	# check if a . or .. shortcut was given and make an absolute path if it was
	match = re.match('\.|\.\.|~', path)
	if match:
		path = os.path.abspath(path)

	if os.path.exists(path):
		return True
	else:
		return False


# ### Path Setup ###
def io_path_setup(i_path, o_path):
	# check if an absolute path was supplied
	i_match = re.match('^/.*$', i_path)

	# check if the input and output paths exist
	if not check_path_exists(i_path):
		print('<ERROR>\nThe supplied input path doesn''t exist, please supply an existing one.\n</ERROR>')
		exit(1)

	if not check_path_exists(o_path):
		os.mkdir(os.path.abspath(o_path))
		print('<INFO>\nThe supplied output path doesn''t exist, but it has been created.\n</INFO>')

	# create absolute input and output paths
	global input_path
	if args.input_path == '.':
		input_path = script_path
	# aboslute path
	elif i_match:
		input_path = i_path
	# relative path
	else:
		input_path = os.path.abspath(i_path)
	# check if a trailing / exists in the path, if not, add it
	match = re.match('^.*/$', input_path)
	if not match:
		input_path += '/'

	# delete output_path contents - lol don't add -rf / you clownz
	rm_command = ['cd', output_path, ';', 'rm', '*']
	if debugging:
		print(rm_command)
	subprocess.call(' '.join(rm_command), shell=True)



# @@@ File Check @@@
# ### Get all files ###
def get_all_files():
	# returned in arbitrary order so we are sorting it
	all_filenames = os.listdir(output_path)
	all_filenames.sort()
	return all_filenames


# ### Remove Non-breaking Spaces ###
# notepad++ searching
# https://en.wikipedia.org/wiki/Non-breaking_space - https://stackoverflow.com/a/2774507
def clean_tika_output():
	all_filenames = get_all_files()
	list_length = len(all_filenames)
	# https://www.regular-expressions.info/python.html & https://stackoverflow.com/a/2774507 (this failed, using sed instead)
	#GNU sed can remove it - https://stackoverflow.com/a/27141959 or https://stackoverflow.com/a/8562661 -r 's/\xc2\xa0//g'
	nbsp_regex = u'\u00A0\u202F\u2007\u2060'.encode("utf8")

	sed_output_path = output_path + 'sed_output'
	cat_output_path = output_path + 'cat_output'

	for i in range(list_length):
		current_file = []
		# 1) remove non-breaking space chars
		# https://docs.python.org/2/library/subprocess.html#module-subprocess
		sed_command = ['sed', '-r', 's/\xc2\xa0//g', '"' + output_path + all_filenames[i] + '"', '>', sed_output_path + str(i + 0.01)]
		if debugging:
			all_filenames[i]
			print(sed_command)
		# https://codereview.stackexchange.com/a/162816
		subprocess.call(' '.join(sed_command), shell=True)
		# 2) Remove lines with spaces only
		sed_command = ['sed', '-r', 's/^[[:blank:]]*$//g', sed_output_path + str(i + 0.01), '>', sed_output_path + str(i + 0.02)]
		if debugging:
			print(sed_command)
		subprocess.call(' '.join(sed_command), shell=True)
		# 3) Remove control chars
		sed_command = ['sed', '-r', 's/[[:cntrl:]]//g', sed_output_path + str(i + 0.02), '>', sed_output_path + str(i + 0.03)]
		if debugging:
			print(sed_command)
		subprocess.call(' '.join(sed_command), shell=True)
		# 4) Remove base64 binary attachments
		sed_command = ['sed', '-r', 's/^[[:punct:]A-Za-z0-9]+$//g', sed_output_path + str(i + 0.03), '>', sed_output_path + str(i + 0.04)]
		if debugging:
			print(sed_command)
		subprocess.call(' '.join(sed_command), shell=True)
		# 5) remove consecutive empty lines
		cat_command = ['cat', '-s', sed_output_path + str(i + 0.04), '>', cat_output_path + str(i + 0.01)]
		if debugging:
			print(sed_command)
		subprocess.call(' '.join(cat_command), shell=True)
		# 6) Save processing
		subprocess.call('cat ' + cat_output_path + str(i + 0.01) + ' > ' + '"' + output_path + all_filenames[i] + '"', shell=True)
		# 7) cleanup
		rm_command = ['rm', sed_output_path + str(i) + '.*', cat_output_path + str(i) + '.*']
		if debugging:
			print(rm_command)
		subprocess.call(' '.join(rm_command), shell=True)
		# 8) get output
		output = subprocess.check_output(['cat', output_path + all_filenames[i]])
		# remove the data added during tika processing (.txt extension and final newline)
		current_file.append(re.sub('.txt$', '', all_filenames[i]))
		file_contents = re.sub('\n$', '', output)
		current_file.append(file_contents)
		if debugging:
			print(current_file)
		final_output.append(current_file)


def create_csv():
	length = len(final_output)
	delimiter = ','
	quote = '"'
	with open(output_path + final_file, 'wt') as output_file:
		# write all entries in final_output
		for i in range(length):
			if debugging:
				print(final_output[i])
			# need to use regex to remove the final newline, so we can enclose the string properly for database loading
			if debugging:
				print(final_output[i][0] + ', ' + final_output[i][1])
			output_file.write(quote + final_output[i][0] + quote + delimiter + quote + re.sub('\n$', '', final_output[i][1]) + quote + '\n')
	print(output_path + final_file + ' created.')



# @@@ Command Arguments @@@
# create the argument parser, which has a free -h  and --help
parser = argparse.ArgumentParser(
	description='Use Apache Tika to try and extract "human readable" content from a variety of files. The any binary represented as base64 is removed, so are consecutive blank lines. Post processing is done with GNU core utils on Linux.'
)
# add positional and optional arguments
parser.add_argument(
	'input_path'
	,help="Enter the path that you want to process with Apache Tika."
	+ " A single dot can be used for the current directory."
	+ " An aboslute or relative path can also be used."
)
parser.add_argument(
	'-o'
	,'--output'
	,help='Optional, the default will be XML if this is omitted. Enter the output type, this can be XML, HTML, and Text.'
	,choices=['x', 'h', 't']
)
args = parser.parse_args()


# @@@ Program @@@
print('@@@ Apache Tika Text Extraction @@@')
print('### Command Arguments ###')

# process the supplied directories
print('Processing positional arguments (directories).')
io_path_setup(args.input_path, output_path)
print('Reading from ' + input_path)
print('Deleting all files in and then writing to ' + output_path)

# check the optional argument
print('\nProcessing optional arguments (output format).')
if args.output is not None:
	tika_output_format = args.output
output_type = ''
if tika_output_format == 'x':
	output_type = 'text/xml'
elif tika_output_format == 't':
	output_type = 'text/plain'
	# exclude metadata
	tika_output_format = 'T'
elif tika_output_format == 'h':
	output_type = 'text/html'
print('Writing output as ' + output_type)

# run Apache Tika
print('\n### Running Apache Tika ###')
print('Creating command line.')
#arguments = ["java", "-jar", tika_path + tika_file, "-i", input_path, "-o", output_path, , "-numConsumers", tika_threads]
arguments = ["java", "-jar", tika_path + tika_file, "-i", input_path, "-o", output_path, "-" + tika_output_format, "-numConsumers", str(tika_threads)]
print('Executing command line.\n')
#print("java -jar " + tika_path + tika_file + " -i " + input_path + " -o " + output_path + " -" + tika_output_format + " -numConsumers " + str(tika_threads))
subprocess.call(arguments)

print('\n### Running Post Processing Data Cleansing ###')
clean_tika_output()
print('Done.')

print('\n### Creating CSV File ###')
create_csv()

