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

url = "https://www.gutenberg.org/files/11/11-0.txt"
absolute_file_path = "/media/veracrypt1/Development/io-files/alice.txt"

try:
	# Read the file as utf-8
	with open(absolute_file_path, encoding="utf-8") as file:
		contents = file.read()
except FileNotFoundError:
	print(f"Couldn't find the file\n{absolute_file_path}\n")
else:
	words = contents.split()
	number_of_words = len(words)
	print(f"There are around {number_of_words} in the file\n{absolute_file_path}\n")
