#!/usr/bin/env python
# @author: dhall
# @started : 2017-12-05
# @updated : 2017-12-13

# import required modules
import argparse, mimetypes, os, commands, re, time, datetime, pipes, email, sys, threading
# xml and html parsing - http://infohost.nmt.edu/tcc/help/pubs/pylxml/web/etree-view.html
from lxml import etree

# @@@ INNER CLASS @@@
# https://stackoverflow.com/a/39504463
class Spinner:
	busy = False
	delay = 0.1

	@staticmethod
	def spinning_cursor():
		while 1: 
			for cursor in '|/-\\': yield cursor

	def __init__(self, delay=None):
		self.spinner_generator = self.spinning_cursor()
		if delay and float(delay): self.delay = delay

	def spinner_task(self):
		while self.busy:
			sys.stdout.write(next(self.spinner_generator))
			sys.stdout.flush()
			time.sleep(self.delay)
			sys.stdout.write('\b')
			sys.stdout.flush()

	def start(self):
		self.busy = True
		threading.Thread(target=self.spinner_task).start()

	def stop(self):
		sys.stdout.write('\b')
		sys.stdout.flush()
		self.busy = False
		time.sleep(self.delay)

# create a progress spinner
spinner = Spinner()

# @@@ GLOBAL VARIABLES @@@
# defining some common extensions which will be used for file inclusion / exclusions - https://www.file-extensions.org/extensions/common-file-extension-list
email_extensions = ('eml', 'msg')
doc_extensions = ('doc', 'docm', 'docx', 'dot', 'dotm', 'dotx', 'odt', 'ott', 'rtf')
code_extensions = ('asm', 'asp', 'aspx', 'bat', 'class', 'css', 'htm', 'html', 'inc', 'jad', 'java', 'js', 'json', 'jsp', 'lib', 'o', 'php', 'py', 'rc', 'rss', 'scpt', 'sh', 'src', 'vbs', 'xcodeproj', 'xml', 'xsd', 'xsl', 'xslt')
source_code_extensions = ()
script_path = os.getcwd() + '/'
target_path = ''
mime_type_filter = ''
all_filenames_sorted = []
match_counts = [['text', 0], ['email', 0], ['documents', 0]]
final_output = []

# @@@ FUNCTIONS @@@
# ### Setup Constants ###
def mime_text():
	return 'text/.*'
# ### Setup Mime & Paths ###
def mime_setup():
	# ### MIME Setup ###
	# initialise all the MIME types known to the system - https://docs.python.org/2/library/mimetypes.html#
	mimetypes.init()

def target_path_setup(args_path):
	# ### Target Path Setup ###
	#check if an absolute path was supplied
	match = re.match('^/.*$', args_path)

	# current directory
	# global keyword is needed here so we assign to the global variable and not a local variable
	global target_path
	if args.target_path  == '.':
		target_path = script_path
	# aboslute path
	elif match:
		target_path = args_path
	# relative path
	else:
		target_path = script_path + args_path

	# check if a trailing / exists in the path, if not, add it
	match = re.match('^.*/$', target_path)
	if not match:
		target_path += '/'

# ### Get All Files In A Directory ###
def get_all_filenames_sorted(target_path):
	# create a list of all files in the current directory -  https://docs.python.org/2/library/os.html#files-and-directories
	# change the script's working diretory, otherwise it won't work outside the current working directory
	os.chdir(target_path)
	all_filenames = os.listdir(target_path)
	# sort the list because it is returned in an arbitrary order
	# sort() returns None, so don't do the assignment on the same line - https://stackoverflow.com/a/11355401
	all_filenames.sort()
	return all_filenames

# ### Extract Plaintext Text ###
def extract_text_from_text_file(filename):
	
	# store the file information
	current_file = []
	current_file.append(filename)
	
	# create a file object (reading text) that will automatically close- https://docs.python.org/2/library/stdtypes.html#file-objects
	current_file_all_lines = []
	with open(target_path + filename, 'rt') as input_file:
		# store all the lines (including newlines) in the file into a list
		current_file_all_lines = input_file.readlines()
		# write all the list to a string
		current_file.append(''.join(current_file_all_lines))
		# save the processed file output
		final_output.append(current_file)
	
	#print(current_file)

# ### Extract Email Text ###
# sourced from https://stackoverflow.com/a/32840516
def extract_text_from_email(filename, mime_type):

	#print(filename + ' ' + mime_type)	
	# open the file and create a file object, the file will automatically close
	with open(target_path + filename, "rt") as input_file:

		# get a message object - https://docs.python.org/2/library/email.parser.html
		an_email = email.message_from_file(input_file)
		body = ""

		# check if email is a multipart message - https://en.wikipedia.org/wiki/MIME#Multipart_messages	
		if an_email.is_multipart():
			print('Multi: ' + filename)
			for part in an_email.walk():
				# https://en.wikipedia.org/wiki/MIME#Content-Type
				part_content_type = part.get_content_type()
				# https://en.wikipedia.org/wiki/MIME#Content-Disposition
				part_content_disposition = str(part.get('Content-Disposition'))
				#print('multi-part:' + filename + ' - ' + part_content_type + ' ' + part_content_disposition)

				# try to extract text/plain multiparts but skip if they are attachments
				mime_is_text = re.search(r"text/.*", part_content_type)
				if part_content_type == 'text/plain' and 'attachment' not in part_content_disposition:
					body = part.get_payload(decode=True)  # decode
					break
				# sometimes the message is still in HTML... I hate you apple MailRaider.
				elif part_content_type == 'text/html' and 'attachment' not in part_content_disposition:
					# try to parse the html - No longer using as too many errors, just saving as is
					body = part.get_payload(decode=True)
					body = etree.parse(body)
					break	

				elif mime_is_text and 'attachment' not in part_content_disposition:
					body = part.get_payload(decode=True)
					break

		# not multipart - i.e. plain text, no attachments, keeping fingers crossed
		else:
			#print('!!! file = ' + filename + ' !!!')
			# if this MIME is encountered, there might be attachments extract at the same time (i.e. binary to base64 = long string!)
			if mime_type == 'Composite Document File V2 Document, No summary info':
				# use strings to extract the string only - https://stackoverflow.com/a/15382675
				print('Compo: ' + filename)
				body = (commands.getoutput("strings -e l " + pipes.quote(filename)))
			# another MIME where there might be attachments and needs to be processed like above
			elif mime_type == 'text/html': #'application/octet-stream':
				print('HTML: ' + filename)
				parsed_html = etree.parse(str(en_email))
			else:
				print('plaintext: ' + filename)
			#	body = an_email.get_payload(decode=True)
			#	print(an_email)
	
		# store the file information
		current_file = []
		current_file.append(filename)
		current_file.append(body)
		final_output.append(current_file)
	
	#print(current_file)

# ### Extract Document Text ###
def extract_text_from_doc(filename):
	return None


# @@@ PROGRAM @@@
# ### CMD ARGUMENTS ###
# create the argument parser - https://docs.python.org/2/library/argparse.html & https://docs.python.org/2/howto/argparse.html#id1
parser = argparse.ArgumentParser(description='Try to extract the text contents of all "human readable" files in the current or specified directory based on the supplied type. MIME types are used to identify files.  When using \'text\' emails will be ignored, because file attachments converted to base64 get picked up.  When using \'all\', the processing order will be \'text\' files, \'email\' files, and finally office suite \'doc\'uments.')
# add arguments, define a short and long optional argument, provide a help text, and define the valid choices.
parser.add_argument('target_path', help="Enter the path that you want to search.  You can use '.' for the current directory.")
parser.add_argument('-t', '--type', help='Default is text', choices=['all', 'code', 'doc', 'email', 'text'])
# parse the arguments - this gives us -h and --help for free, which prints a nicely formatted help message.  We are also storing this for use later, if nothnig is supplied it will be None
args = parser.parse_args()

# check if a file type argument was given, if not use text/* as the MIME type.  Must use long argument for check
print('@@@ Optional Argument(s) @@@')
if args.type != None:
	mime_type_filter = args.type
	print('--type supplied - processing ' + mime_type_filter)
else:
	mime_type_filter = 'text'
	print('--type not supplied, processing ' + mime_type_filter)
mime_setup()

# ### FILE PROCESSING ###
# *** Setup Target Path ***
target_path_setup(args.target_path)

# *** Get Source Filenames  ***
all_filenames_sorted = get_all_filenames_sorted(target_path)
print('\n@@@ File Processing @@@\nSearching ' + target_path)

# *** Process Source Files ***
# display progress spinner
spinner.start()

# loop through the filenames and determine MIME type and extension
for i in range(len(all_filenames_sorted)):
	current_file = []
	# get the current filename
	current_filename = all_filenames_sorted[i]
	current_file.append(current_filename)
	# get the current extension if it exists, otherwise store nothing
	pattern = re.compile(r"^.*(?<=\.)([0-9A-Za-z]+)$")
	match = pattern.search(current_filename)
	if match:
		current_file_extension = match.group(1)
	else:
		current_file_extension = ''
	#current_file_extension = re.sub(r"^.*(?<=\.)([0-9A-Za-z]+)$", '\\1', current_filename)
	# convert the extension to lower case
	current_file.append(current_file_extension.lower())
	# get the current mimetype of the file
	# this doesn't work on files without extensions) - https://docs.python.org/2/library/mimetypes.html#mimetypes-objects
	# current_file_mime = str(mimetypes.MimeTypes().guess_type(all_filenames[i]))
	# in Python 2 you need to use pipes.quote() - https://docs.python.org/2/library/pipes.html#pipes.quote
	current_file_mime = (commands.getoutput('file -b --mime-type ' + pipes.quote(current_filename)))
	# get the part of the string that we care about 'mime/type' - No longer need because -b does this for us
	# current_file_mime = re.sub(r"^.* :([0-9A-Za-z]/.*).*$", '\\1',  current_file_mime)
	current_file.append(current_file_mime)
	#print(current_file)

	# check to see if the file has a text mime
	 
	#print(text_mime_test)

	# check to see if plain text only
	is_plain_text = False
	#mime_is_text = re.search(r"text/.*", current_file_mime)
	#if mime_is_text:
	if current_file_mime == 'text/plain':
		is_plain_text = True

	# check to see if the file has an email extension
	is_email = False
	for i in range(len(email_extensions)):
		if current_file_extension == email_extensions[i]:
			#print('Email: ' + current_filename + ' MIME: ' + current_file_mime)
			is_email = True
			break

	# check to see if the file has a document mime type
	is_doc = False
	if current_file_mime == 'text/rtf':
		is_doc = True
	if not is_doc:
		for i in range(len(doc_extensions)):
			if current_file_extension == doc_extensions[i]:
				is_doc = True
				break

	# filter based on user argument
	if mime_type_filter == 'all':
		continue
	elif mime_type_filter == 'code':
		continue
	elif (mime_type_filter == 'email' and is_email):
		#print(current_file)
		extract_text_from_email(current_filename, current_file_mime)
		continue
	elif mime_type_filter == 'doc':
		continue
	elif (mime_type_filter == 'text' and not is_email and not is_doc and is_plain_text):
		#print(mime_type_filter + ' found')
		extract_text_from_text_file(current_filename)
		continue

	else:
		continue
		#print("MIME didn't match")

# stop the progress spinner
spinner.stop()

	# check if the target file's mime type matches what we are searching for	
#	mime_test = re.search(r"" + mime_type + "/.*", current_file_mime)
#	if (mime_test):
		# store the current file into the target list
#		process_files.append(all_filenames[i])

# count the matches

# ### SAVE FINAL OUTPUT ###
# get the current timestamp from the UNIX epoch - https://stackoverflow.com/a/13891070
epoch = time.time()
timestamp = datetime.datetime.fromtimestamp(epoch).strftime('%Y-%m-%d %H:%M:%S')

output_type = ''
if(mime_type_filter != 'all'):
	output_type = mime_type_filter
else:
	output_type = 'supported_mime_'

filename = 'all_' + output_type + '_files_@_' + timestamp + '.txt'
output_path = script_path + filename
delimiter = chr(30)
#delimiter = u"\u001E"
quote = '"'
with open(output_path, 'wt') as output_file:
	# write all entries in final_output
	for i in range(len(final_output)):
		# need to use regex to remove the final newline, so we can enclose the string properly for database loading
		output_file.write(quote + final_output[i][0] + quote + delimiter + quote + re.sub('\n$', '', final_output[i][1]) + quote + '\n')
print('\n'+ output_path + ' created.')
