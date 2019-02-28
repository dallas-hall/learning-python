#!/usr/bin/python3

import logging, sys, os, time, re, hashlib
from pathlib import Path, PurePath


# Functions
def check_answer(message):
	while True:
		print(message)
		answer = input().lower()
		if answer == 'y':
			return 'y'
		elif answer == 'n':
			return 'n'
		else:
			print('Invalid input, try again.')


def get_input_path():
	while True:
		print('Enter the input path of the files to hash. Relative and canonical paths will be transformed into aboslute paths.')
		answer = input()
		result = check_answer('Input path is\n' + answer + '\nIs this correct?')
		if result == 'y':
			return answer


def get_output_path():
	while True:
		print('Enter the output path of the files to hash. Relative and canonical paths will be transformed into aboslute paths.')
		answer = input()
		result = check_answer('Output path is\n' + answer + '\nIs this correct?')
		if result == 'y':
			return answer


def get_absolute_path(input_path):
	# check if a . or .. shortcut was given and make an absolute path if it was
	match = re.match('^~', input_path)
	if match:
		return Path(input_path).expanduser()

	match = re.match('^\\.', input_path)
	if match:
		return Path.resolve(Path(input_path))

	match = re.match('^\\.\\.', input_path)
	if match:
		return Path.resolve(Path(input_path))

	return Path.resolve(Path(input_path))


# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.005)

# Get user input for paths
input_path = get_absolute_path(get_input_path())
output_path = get_absolute_path(get_output_path())

if debugging:
	logging.debug('input_path is\n' + str(input_path))
	logging.debug('output_path is\n' + str(output_path))

