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

absolute_file_path = "/media/veracrypt1/Development/io-files/pi_million_digits.txt"
with open(absolute_file_path) as file_object:
	pi_million_digits = file_object.read()

birthday = input("Enter your birthday [ddmmyy]: ")
if birthday in pi_million_digits:
	print("Your birthday in format of ddmmyy appears in the first million digits of pi :)")
else:
	print("Your birthday in format of ddmmyy doesn't appear in the first million digits of pi :(")
