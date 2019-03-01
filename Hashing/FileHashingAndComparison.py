#!/usr/bin/python3

import logging, sys, os, time, re, hashlib, pprint, json
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


def hash_files(algorithm):
	for file in Path(input_path).iterdir():
		choices = {
			'blake2b': hashlib.blake2b(Path(file).read_bytes()).hexdigest(),
			'blake2s': hashlib.blake2s(Path(file).read_bytes()).hexdigest(),
			'md5': hashlib.md5(Path(file).read_bytes()).hexdigest(),
			'sha1': hashlib.sha1(Path(file).read_bytes()).hexdigest(),
			'sha224': hashlib.sha224(Path(file).read_bytes()).hexdigest(),
			'sha256': hashlib.sha256(Path(file).read_bytes()).hexdigest(),
			'sha384': hashlib.sha384(Path(file).read_bytes()).hexdigest(),
			'sha3_224': hashlib.sha3_224(Path(file).read_bytes()).hexdigest(),
			'sha3_256': hashlib.sha3_256(Path(file).read_bytes()).hexdigest(),
			'sha3_384': hashlib.sha3_384(Path(file).read_bytes()).hexdigest(),
			'sha3_512': hashlib.sha3_512(Path(file).read_bytes()).hexdigest(),
			'sha512': hashlib.sha512(Path(file).read_bytes()).hexdigest(),
			'shake_128': hashlib.shake_128(Path(file).read_bytes()).hexdigest(128),
			'shake_256': hashlib.shake_256(Path(file).read_bytes()).hexdigest(256)
		}

		algorithm_output = choices.get(hashing_algorithm, hashlib.md5(Path(file).read_bytes()).hexdigest())
		hashed_files[file.name] = {
			'checked': False,
			'hash': algorithm_output,
			'hashAlgorithm': algorithm,
			'duplicateFiles': []
		}

		if debugging:
			logging.debug(file)
			logging.debug(file.name)
			logging.debug(str(file) + ' is\n' + algorithm_output)
			logging.debug(algorithm)


def check_for_duplicate_hashes():
	for this_file, this_metadata in hashed_files.items():
		if not this_metadata['checked']:
			this_metadata['checked'] = True
			for that_file, that_metadata in hashed_files.items():
				if not that_metadata['checked'] and this_metadata['hash'] == that_metadata['hash']:
					this_metadata['duplicateFiles'].append(that_file)
					that_metadata['duplicateFiles'].append(this_file)
		if debugging:
			logging.debug('file is ' + str(this_file))
			logging.debug('metadata is ' + str(this_metadata))


# Define logging and pretty print output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')
pp = pprint.PrettyPrinter()

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
