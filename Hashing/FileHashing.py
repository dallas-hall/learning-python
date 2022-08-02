#!/usr/bin/python3

import logging, sys, os, time, hashlib
from pathlib import Path

# Define logging output
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.005)

input_path = Path.cwd()
logging.debug('Shortcut')
time.sleep(.005)
for file in Path(input_path).iterdir():
	file_binary = Path(file).read_bytes()
	print(str(file) + ' is\n' + hashlib.blake2b(Path(file).read_bytes()).hexdigest())

logging.debug('Long')
time.sleep(.005)
for file in Path(input_path).iterdir():
	file_binary = Path(file).read_bytes()
	hash = hashlib.blake2b()
	hash.update(file_binary)
	print(str(file) + ' is\n' + hash.hexdigest())


def get_hash_algorithm_broken(algorithm):
	return {
	'blake2b': hashlib.blake2b(),
	'blake2s': hashlib.blake2s(),
	'md5': hashlib.md5(),
	'sha1': hashlib.sha1(),
	'sha224': hashlib.sha224(),
	'sha256': hashlib.sha256(),
	'sha384': hashlib.sha384(),
	'sha3_224': hashlib.sha3_224(),
	'sha3_256': hashlib.sha3_256(),
	'sha3_384': hashlib.sha3_384(),
	'sha3_512': hashlib.sha3_512(),
	'sha512': hashlib.sha512(),
	'shake_128': hashlib.shake_128(),
	'shake_256': hashlib.shake_256()
	}.get(algorithm, hashlib.md5())

logging.debug('Long with pseudo-switch statement')
time.sleep(.005)
hash_algorithm = 'blake2b'
hash = get_hash_algorithm_broken(hash_algorithm)
for file in Path(input_path).iterdir():
	file_binary = Path(file).read_bytes()
	hash.update(file_binary)
	print(str(file) + ' is\n' + hash.hexdigest())


def get_file_hash(algorithm, data):
	return hashlib.new(algorithm, data).hexdigest()


logging.debug('Long with hashlib.new')
time.sleep(.005)
for file in Path(input_path).iterdir():
	hash = get_file_hash(hash_algorithm, Path(file).read_bytes())
	print(str(file) + ' is\n' + hash)
