#!/usr/bin/python3

import logging, sys, os, time, re, hashlib, pprint
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


def get_absolute_path(path):
	# check if a . or .. shortcut was given and make an absolute path if it was
	match = re.match('^~', path)
	if match:
		return Path(path).expanduser()

	match = re.match('^\\.', path)
	if match:
		return Path.resolve(Path(path))

	match = re.match('^\\.\\.', path)
	if match:
		return Path.resolve(Path(path))

	return Path.resolve(Path(path))


def get_hashing_algorithm():
	while True:
		print('Enter the hashing algorithm that you want to use from the list below.')
		print(guaranteed_hash_algorithms)

		answer = input()
		result = check_answer('Hashing algorithm is \'' + answer + '\', is this correct?')

		if result == 'y' and is_valid_hash_algorithm(answer):
			return answer
		elif result == 'y' and not is_valid_hash_algorithm(answer):
			print('Invalid algorithm, try again.')


def is_valid_hash_algorithm(algorithm):
	return algorithm.lower() in guaranteed_hash_algorithms



# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.005)

# System guaranteed algorithms.
guaranteed_hash_algorithms = sorted(hashlib.algorithms_guaranteed)

# Get user input for paths
input_path = get_absolute_path(get_input_path())
output_path = get_absolute_path(get_output_path())
hashing_algorithm = get_hashing_algorithm()

if debugging:
	#logging.debug('input_path is\n' + str(input_path))
	#logging.debug('output_path is\n' + str(output_path))
	logging.debug('hashing_algorithm is\n' + str(hashing_algorithm))

