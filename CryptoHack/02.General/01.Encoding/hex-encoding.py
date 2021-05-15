#!/usr/bin/env python3

# SECOND CHALLENGE

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

# When we encrypt something the resulting ciphertext commonly has bytes which are not printable ASCII characters.
# If we want to share our encrypted data, it's common to encode it into something more user-friendly and portable across different systems.
# Included below is a flag encoded as a hex string. Decode this back into bytes to get the flag.
hex_str = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'

# https://docs.python.org/3/library/binascii.html#binascii.unhexlify
flag_binary = binascii.unhexlify(hex_str)
print(flag_binary)

# https://docs.python.org/3/library/stdtypes.html#bytes.decode
flag = flag_binary.decode()
print(flag)
