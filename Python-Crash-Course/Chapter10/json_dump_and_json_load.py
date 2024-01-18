#!/usr/bin/env python3
import logging, sys, os, time
import json
from random import randint
from pathlib import Path

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.100)

print('# 2nd Edition Code')
output_numbers = []
for i in range(10):
	# Generate a random number between 2 numbers, inclusive.
	output_numbers.append(randint(1, 100))
print('From Python:')
print(output_numbers)

absolute_file_path = "/ssd/Development/random-files-for-dev-io/prn-numbers.json"
with open(absolute_file_path, 'w') as file:
	json.dump(output_numbers, file)
	file.write("\n")
with open(absolute_file_path, 'r') as file:
	input_numbers = json.load(file)
print('From JSON:')
print(input_numbers)

print('# 3rd Edition Code')
output_numbers = []
for i in range(10):
	# Generate a random number between 2 numbers, inclusive.
	output_numbers.append(randint(1, 100))
print('From Python:')
print(output_numbers)

path = Path(absolute_file_path)
contents = json.dumps(output_numbers)
path.write_text(contents)
contents = path.read_text()
numbers = json.loads(contents)
print('From JSON:')
print(numbers)
