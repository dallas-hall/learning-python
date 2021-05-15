#!/usr/bin/python3
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

# https://en.wikipedia.org/wiki/Bitwise_operation#XOR - XOR is a bitwise operator which returns 0 if the bits are the same, and 1 otherwise.
# In textbooks the XOR operator is denoted by ⊕, but in most challenges and programming languages you will see the caret ^ used instead.
# For longer binary numbers we XOR bit by bit: 0110 ^ 1010 = 1100. We can XOR integers by first converting the integer from decimal to binary.
# We can XOR strings by first converting each character to the integer representing the Unicode character.
# Given the string "label", XOR each character with the integer 13. Convert these integers back to a string and submit the flag as crypto{new_string}.
input_str = "label"
output_str = ""
xor_int = 13

# https://docs.python.org/3/reference/expressions.html#binary-bitwise-operations
for i in range(len(input_str)):
	# Convert the char to an int codepoint - https://docs.python.org/3/library/functions.html#ord
	# XOR the 2 ints together and convert output to a char
	output_str += chr(ord(input_str[i]) ^ xor_int)

print(output_str)
print('crypto{' + output_str + '}')
