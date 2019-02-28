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

for file in Path(input_path).iterdir():
	file_binary = Path(file).read_bytes()
	print(str(file) + ' is\n' + hashlib.blake2b(Path(file).read_bytes()).hexdigest())

for file in Path(input_path).iterdir():
	file_binary = Path(file).read_bytes()
	hash = hashlib.blake2b()
	hash.update(file_binary)
	print(str(file) + ' is\n' + hash.hexdigest())
