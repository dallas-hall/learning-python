#!/usr/bin/python3
import logging, sys, os, time

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.100)

print("A tuple is an immutable list, using the () notation.")
hex_digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f')
print(hex_digits)
print(hex_digits[:10])
print(hex_digits[10:])

print("Assign a new value to the tuple variable. This will replace the existing tuple.")
# A tuple with one element must have a comma after it.
hex_digits = (1,)
print(hex_digits)

# This will error as tuples are immutable
hex_digits[0] = 0
