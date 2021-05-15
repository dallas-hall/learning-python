#!/usr/bin/env python3

# FIRST CHALLENGE

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

# ASCII is a 7-bit encoding standard which allows the representation of text using the integers 0-127.
# Using the below integer array, convert the numbers to their corresponding ASCII characters to obtain a flag.
ascii_chars = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
flag = ''

for i in range(len(ascii_chars)):
    flag += chr(ascii_chars[i])

print(flag)

