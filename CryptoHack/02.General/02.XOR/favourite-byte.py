#!/usr/bin/python3

# THIRD CHALLENGE

import logging
import os
import sys
import time
import binascii

from pwn import xor
from Crypto.Util.number import long_to_bytes

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = False
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.005)

# I've hidden my data using XOR with a single byte. Don't forget to decode from hex first.
hex_str = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
binary_str = binascii.unhexlify(hex_str)
print('binary_str: ')
print(binary_str)

binary_number = 0
for i in range(256):
	if debugging:
		# Convert an in to a binary number - https://docs.python.org/3/library/functions.html#bin
		print(i)
		print(bin(i))
		print(long_to_bytes(i))
	# Ignore invalid encodings - https://docs.python.org/3/library/stdtypes.html#bytes.decode &
	# https://docs.python.org/3/library/codecs.html#error-handlers
	xor_result = xor(binary_str, long_to_bytes(i)).decode(errors="ignore")
	if 'crypto' in xor_result:
		print("i:" + str(i))
		print("i as binary: " + str(bin(i)))
		print("i as bytes: ")
		print(long_to_bytes(i))
		print("flag: " + xor_result)

