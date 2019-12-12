#!/usr/bin/python3
import logging, sys, os, time
import json
from random import randint

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.001)

output_numbers = []
for i in range(10):
	# Generate a random number between 2 numbers, inclusive.
	output_numbers.append(randint(1, 100))
print(output_numbers)

absolute_file_path = "/media/veracrypt1/Development/io-files/prn-numbers.json"
with open(absolute_file_path, 'w') as file:
	json.dump(output_numbers, file)
	file.write("\n")

with open(absolute_file_path, 'r') as file:
	input_numbers = json.load(file)

print(input_numbers)