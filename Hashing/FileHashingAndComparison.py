#!/usr/bin/python3

import logging, sys, os, time, re, hashlib, json
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
		answer = get_absolute_path(input())
		result = check_answer('Input path is\n' + str(answer) + '\nIs this correct?')
		if result == 'y':
			return answer


def get_output_path():
	while True:
		print('Enter the output path of the files to hash. Relative and canonical paths will be transformed into aboslute paths.')
		answer = get_absolute_path(input())
		result = check_answer('Output path is\n' + str(answer) + '\nIs this correct?')
		if result == 'y':
			return answer


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


def get_absolute_path(path):
	# check if a . or .. shortcut was given and make an absolute path if it was
	match = re.match('^~', path)
	if match:
		return Path(path).expanduser()

	match = re.match('^\.|^\.\.', path)
	if match:
		return Path.resolve(Path(path))

	return Path.resolve(Path(path))


def get_all_files_absolute_paths(directory):
	return [PurePath.joinpath(directory, file) for file in Path(directory).iterdir()]


def get_file_hash(algorithm, data):
	if debugging:
		hashing_algorithm = hashlib.new(algorithm)
		hashing_algorithm.update(data)
		logging.debug('(long) hash is ' + hashing_algorithm.hexdigest())
		hashing_algorithm = hashlib.new(algorithm, data).hexdigest()
		logging.debug('(short) hash is ' + hashing_algorithm)
	return hashlib.new(algorithm, data).hexdigest()


def hash_files(algorithm):

	for file in Path(input_path).iterdir():
		#hash_output = hashlib.new(algorithm, Path(file).read_bytes()).hexdigest()
		hash_output = get_file_hash(algorithm, Path(file).read_bytes())

		if hashed_files == {}:
			hashed_files[hash_output] = {
				'hashAlgorithm': algorithm,
				'filenames': [file.name]
			}
		elif hash_output in hashed_files:
			hashed_files[hash_output]['filenames'].append(file.name)
		else:
			hashed_files[hash_output] = {
				'hashAlgorithm': algorithm,
				'filenames': [file.name]
			}

		if debugging:
			logging.debug(file)
			logging.debug(file.name)
			logging.debug(str(file) + ' is\n' + hash_output)

	if debugging:
		logging.debug(str(hashed_files))


def check_for_duplicate_hashes():
	return None


def print_dictionary():
	print(json.dumps(hashed_files, indent=4, sort_keys=False))


# Define logging and pretty print output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.005)

# System guaranteed hashing algorithms.
guaranteed_hash_algorithms = sorted(hashlib.algorithms_guaranteed)

# Get user answers for paths and hashing algorithm
input_path = get_input_path()
output_path = get_output_path()
hashing_algorithm = get_hashing_algorithm()
if debugging:
	time.sleep(.005)
	logging.debug('input_path is\n' + str(input_path))
	logging.debug('output_path is\n' + str(output_path))
	logging.debug('hashing_algorithm is\n' + str(hashing_algorithm))

# Hash all files in the base directory of the input_path (no recursive file walking)
hashed_files = {}
hash_files(hashing_algorithm)
check_for_duplicate_hashes()
print_dictionary()
