#!/usr/bin/python3

# FORTH CHALLENGE

import binascii
import logging
import os
import sys
import time

from pwn import xor

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.001)

# I've encrypted the flag with my secret key, you'll never be able to guess it.
# Remember the flag format and how it might help you in this challenge!

hex_str = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
binary_str = binascii.unhexlify(hex_str)
print('binary_str: ')
print(binary_str)
print('len(binary_str): ')
print(len(binary_str))

crypto = 'crypto{'
crypto_binary = crypto.encode()
print('crypto_binary :')
print(crypto_binary)

xor_result = xor(binary_str, crypto_binary)
print('xor_result: ')
print(xor_result) # <- this XOR result was the key to me trying the next string

key = 'myXORkey'
key_binary = key.encode()
xor_result = xor(binary_str, key_binary)
print('xor_result: ')
print(xor_result)
