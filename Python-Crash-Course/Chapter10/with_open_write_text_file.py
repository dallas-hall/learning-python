#!/usr/bin/env python3
import logging, sys, os, time

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.100)

absolute_file_path = "/ssd/Development/random-files-for-dev-io/python-crash-course-3e-chapter-10-output.txt"
# Use 'w' which is write mode. Which will overwrite an existing file.
with open(absolute_file_path, 'w') as file_object:
	file_object.write("I love programming, particularly in Python and C.\n")

# Use 'a' which is append mode. It will append to an existing file.
with open(absolute_file_path, 'a') as file_object:
	file_object.write("I do like other languages too, just not as much.\n")
