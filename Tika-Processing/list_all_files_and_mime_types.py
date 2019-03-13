#!/usr/bin/env python
# @author: dhall - 2017-12-05

# import required modules
import argparse, mimetypes, os, commands, re, time, datetime, pipes

# @@@ CMD ARGUMENTS @@@
# create the argument parser - https://docs.python.org/2/library/argparse.html & https://docs.python.org/2/howto/argparse.html#id1
parser = argparse.ArgumentParser(description='Try to extract the text contents of all files in the current directory based on the supplied type. The supplied type is converted into a MIME type and the file is found that way.')
# add arguments, define a short and long optional argument, provide a help text, and define the valid choices.
parser.add_argument('target_path', help="Enter the path that you want to search.  You can use '.' for the current directory.")
parser.add_argument('-t', '--type', help='Default is text', choices=['text', 'code', 'doc'])
# parse the arguments - this gives us -h and --help for free, which prints a nicely formatted help message.  We are also storing this for use later, if nothnig is supplied it will be None
args = parser.parse_args()

# check if a file type argument was given, if not use text/* as the MIME type.  Must use long argument for check
mime_type = ''
print('@@@ Optional Argument(s) @@@')
if args.type:
	mime_type = str(args.type)
	print('--type supplied as ' +  mime_type)

else:
	mime_type = 'text'
	print('--type not supplied, using ' + mime_type)

# @@@ FILE PROCESSING @@@
# ### MIME Setup ###
# initialise all the MIME types known to the system - https://docs.python.org/2/library/mimetypes.html#
mimetypes.init()

# ### Create Source and Target Paths ###
# get the script's execution path for later & update the target path
script_path = os.getcwd() + '/'
target_path =''

#check if an absolute path was supplied
match = re.match('^/.*$', args.target_path)

# current directory
if args.target_path  == '.':
	target_path = script_path
# aboslute path
elif match:
	target_path = args.target_path
# relative path
else:
	target_path = script_path + args.target_path

# check if a trailing / exists in the path, if not, add it
match = re.match('^.*/$', target_path)
if not match:
	target_path += '/'
	
# ### Process Target Path ###
# create a list of all files in the current directory -  https://docs.python.org/2/library/os.html#files-and-directories
print('\n@@@ File Processing @@@\nSearching ' + target_path)
# change the script's working diretory, otherwise it won't work outside the current working directory
os.chdir(target_path)
all_filenames = os.listdir(target_path)
# sort the list because it is returned in an arbitrary order
all_filenames.sort()

# ### Get Target Files ###
# loop through the filenames, determine MIME type, and see if it matches the required MIME type. Store if it does
target_files = []
for i in range(len(all_filenames)):
	# get the mimetype of the file (this doesn't work on files without extensions) - https://docs.python.org/2/library/mimetypes.html#mimetypes-objects
	# current_file_mime = str(mimetypes.MimeTypes().guess_type(all_filenames[i]))
	# in Python 2 you need to use pipes.quote() - https://docs.python.org/2/library/pipes.html#pipes.quote
	current_file_mime = (commands.getoutput('file --mime-type ' + pipes.quote(all_filenames[i])))
	# get the part of the string that we care about 'mime/type'
	current_file_mime = re.sub(r"^.*'(" + mime_type + "/.*)'.*$", '\\1',  current_file_mime)
	# check if the mime type matches what we are searching for	
	mime_test = re.search(r"" + mime_type + "/.*", current_file_mime)
	if mime_test:
		# store the current file into the target list
		target_files.append(all_filenames[i])

# count the matches
match_count = 0
for i in range(len(target_files)):
	match_count+=1
print('The search found ' + str(match_count)  + ' files matching ' + mime_type + '.' )

# @@@ TARGET FILE(S) TEXT EXTRACTION @@@
final_output = []
for i in range(len(target_files)):
	# create a file object (reading text) that will automatically close- https://docs.python.org/2/library/stdtypes.html#file-objects
	current_file = []
	all_lines = []
	with open(target_path + target_files[i], 'rt') as file:
		# store all the lines (including newlines) in the file into a list
		all_lines = file.readlines()
		# write all the list to a string
		current_file.append(target_files[i])
		current_file.append(''.join(all_lines))
		final_output.append(current_file)

# @@@ SAVE FINAL OUTPUT @@@
# get the current timestamp from the UNIX epoch - https://stackoverflow.com/a/13891070
epoch = time.time()
timestamp = datetime.datetime.fromtimestamp(epoch).strftime('%Y-%m-%d %H:%M:%S')

filename = 'all_' + mime_type + '_files_@_' + timestamp + '.txt'
output_path = script_path + filename
delimiter = chr(30)
quote = '"'
with open(output_path, 'wt') as file:
	# write all entries in final_output
	for i in range(len(final_output)):
		# need to use regex to remove the final newline, so we can enclose the string properly for database loading
		file.write(quote + final_output[i][0] + quote + delimiter + quote + re.sub('\n$', '', final_output[i][1]) + quote + '\n')
print('\n'+ output_path + ' created.')
