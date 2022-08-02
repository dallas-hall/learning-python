#!/usr/bin/python3

import hashlib
import json
import logging
import re
import shutil
import sys
import time
from pathlib import Path


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


def get_hashing_algorithm():
	while True:
		print('Enter the hashing algorithm that you want to use from the list below.')
		print(available_hash_algorithms)

		answer = input()
		result = check_answer('Hashing algorithm is \'' + answer + '\', is this correct?')

		if result == 'y' and is_valid_hash_algorithm(answer):
			return answer
		elif result == 'y' and not is_valid_hash_algorithm(answer):
			print('Invalid algorithm, try again.')


def is_valid_hash_algorithm(algorithm):
	return algorithm.lower() in available_hash_algorithms


def get_absolute_path(path):
	# check if a . or .. shortcut was given and make an absolute path if it was
	match = re.match('^~', path)
	if match:
		return Path(path).expanduser()

	match = re.match('^\.|^\.\.', path)
	if match:
		return Path.resolve(Path(path))

	return Path.resolve(Path(path))


def get_file_hash(algorithm, data):
	if GLOBAL_DEBUGGING:
		hashing_algorithm_local = hashlib.new(algorithm)
		hashing_algorithm_local.update(data)
		logging.debug('(long) hash is ' + hashing_algorithm_local.hexdigest())
		hashing_algorithm_local = hashlib.new(algorithm, data).hexdigest()
		logging.debug('(short) hash is ' + hashing_algorithm_local)
	return hashlib.new(algorithm, data).hexdigest()


def hash_files(algorithm):
	logging.info('Hashing files in ' + str(INPUT_PATHS))
	time.sleep(.005)

	for input_path in INPUT_PATHS:
		if GLOBAL_DEBUGGING:
			logging.debug("input_path is: " + str(input_path))

		# https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob
		all_paths = sorted(input_path.glob('**/*'))
		for path in all_paths:
			if Path(path).is_dir():
				continue
			hash_output = get_file_hash(algorithm, Path(path).read_bytes())
			if hashed_files == {} or hash_output not in hashed_files:
				hashed_files[hash_output] = {
					'filenames': [str(path)]
				}
			else:
				hashed_files[hash_output]['filenames'].append(str(path))

			if GLOBAL_DEBUGGING:
				logging.debug(path)
				logging.debug(path.name)
				logging.debug(str(path) + ' is\n' + hash_output)

	if GLOBAL_DEBUGGING:
		logging.debug(str(hashed_files))


def write_output():
	logging.info('Saving unique hashed files to ' + str(OUTPUT_PATH))
	time.sleep(.005)
	with open(OUTPUT_PATH / 'file_metadata.txt', 'wt') as metadata_file:
		metadata_file.write(hashing_algorithm + '_hash\tfiles\n')
		for file_hash, file_list in hashed_files.items():
			if SAVE_UNIQUE_FILES:
				# https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.parts
				shutil.copy(file_list['filenames'][0], OUTPUT_PATH / str(Path(file_list['filenames'][0]).parts[-1]))
			# https://stackoverflow.com/a/35119046 & https://stackoverflow.com/a/54345555
			metadata_file.write(str(file_hash) + '\t' + DELIMITER.join(file_list['filenames']) + '\n')
			if GLOBAL_DEBUGGING:
				time.sleep(.005)
				logging.debug('hash is ' + str(hash))
				logging.debug('file list is ' + str(file_list))
				logging.debug('file list is ' + str(file_list['filenames']))
				for files in file_list:
					time.sleep(.005)
					logging.debug('for file ' + str(file_list[files]))


#
# Program
#
# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable GLOBAL_DEBUGGING messages
GLOBAL_DEBUGGING = True
if not GLOBAL_DEBUGGING:
	logging.disable(logging.DEBUG)

# https://docs.python.org/3/library/pathlib.html#pathlib.Path.cwd
SCRIPT_PATH = Path.cwd()
# https://docs.python.org/3/library/sys.html#sys.argv
SCRIPT_NAME = Path(sys.argv[0]).name

# Using https://www.asciitable.com/ control character 31 as a delimiter
DELIMITER = chr(31)
INPUT_PATHS = [
	'/home/dallas/Development/python/Hashing/input1',
	'/home/dallas/Development/python/Hashing/input2'
]
OUTPUT_PATH = SCRIPT_PATH / 'output'
SAVE_UNIQUE_FILES = False

logging.info('Starting ' + SCRIPT_NAME)
# Quick delay so the messages are printed in the correct order
time.sleep(.005)
if GLOBAL_DEBUGGING:
	logging.debug("SCRIPT_PATH = " + str(SCRIPT_PATH))
	logging.debug("SCRIPT_NAME = " + SCRIPT_NAME)

# System available hashing algorithms.
available_hash_algorithms = sorted(hashlib.algorithms_available)
hashing_algorithm = get_hashing_algorithm()

# Convert input paths to absolute paths
for i in range(len(INPUT_PATHS)):
	INPUT_PATHS[i] = get_absolute_path(INPUT_PATHS[i])

# Create output path if it doesn't exist
if not Path.exists(OUTPUT_PATH):
	Path.mkdir(OUTPUT_PATH)

if GLOBAL_DEBUGGING:
	time.sleep(.005)
	logging.debug('INPUT_PATHS is\n' + str(INPUT_PATHS))
	logging.debug('OUTPUT_PATH is\n' + str(OUTPUT_PATH))
	logging.debug('hashing_algorithm is\n' + str(hashing_algorithm))

# Hash all files in the base directory of the input_path (no recursive file walking)
hashed_files = {}
hash_files(hashing_algorithm)
if GLOBAL_DEBUGGING:
	time.sleep(.005)
	logging.debug(json.dumps(hashed_files, indent=4, sort_keys=False))
write_output()
