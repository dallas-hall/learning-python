#!/usr/bin/python3
import logging, sys, os, time, hashlib

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
hash_input = b'This is my hash input lolz.'
# https://crypto.stackexchange.com/a/40262 talks about how Blake2 is better than MD5 for file hashing.
logging.info('Blake2 64 bit optimised hashing.')
time.sleep(.005)
blake2b_hash = hashlib.blake2b()
blake2b_hash.update(hash_input)
print(blake2b_hash.hexdigest())

logging.info('Blake2 32 bit optimised hashing.')
time.sleep(.005)
print(hashlib.blake2s(hash_input).hexdigest())