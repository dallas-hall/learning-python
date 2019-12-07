#!/usr/bin/python3
import logging, sys, os, time

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.001)

absolute_file_path = "/media/veracrypt1/Development/io-files/pi_digits.txt"
with open(absolute_file_path) as file_object:
	# Read the entire file at once
	file_contents = file_object.read()
# read will return an empty string when it gets to the end of file
# This will be displayed as a blank line
print(file_contents)
# Use rstrip to remove the blank line
print(file_contents.rstrip())

with open(absolute_file_path) as file_object:
	# Read the file one line at a time
	for line in file_object:
		# The file has a \n and print() adds it own \n
		print(line)

with open(absolute_file_path) as file_object:
	for line in file_object:
		# Use rstrip to remove the \n from print
		print(line.rstrip())

