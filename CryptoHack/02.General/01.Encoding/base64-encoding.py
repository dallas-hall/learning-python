#!/usr/bin/env python3

# THIRD CHALLENGE

# https://docs.python.org/3/library/base64.html#module-base64
import base64
# https://docs.python.org/3/library/binascii.html
import binascii
import logging
import os
import sys
import time

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.001)

# Another common encoding scheme is Base64, which allows us to represent binary data as an ASCII string using 64 characters.
# One character of a Base64 string encodes 6 bits, and so 4 characters of Base64 encodes three 8-bit bytes.
# Base64 is most commonly used online, where binary data such as images can be easy included into html or css files.
# Take the below hex string, decode it into bytes and then encode it into Base64.
hex_str = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

# https://docs.python.org/3/library/binascii.html#binascii.unhexlify
binary_str = binascii.unhexlify(hex_str)
print(binary_str)

# https://docs.python.org/3/library/base64.html#base64.b64decode
binary_flag = base64.b64encode(binary_str)
flag = binary_flag.decode()

print(flag)
