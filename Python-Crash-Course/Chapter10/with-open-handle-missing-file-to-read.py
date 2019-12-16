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

absolute_file_path = "/media/veracrypt1/Development/io-files/id_rsa"

try:
	# Read the file as utf-8
	with open(absolute_file_path, encoding="utf-8") as file:
		contents = file.read()
except FileNotFoundError:
	print("LOL my rsa ssh key isn't in that folder dawg...")

# crash
with open(absolute_file_path, encoding="utf-8") as file:
	contents = file.read()
