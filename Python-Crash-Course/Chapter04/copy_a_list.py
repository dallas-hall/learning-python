#!/usr/bin/env python3
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

hex_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
print(hex_digits)
print("Copy the entire list with [:] into a new list")
new_list = hex_digits[:]
print(new_list)

print("Associate the list with assignment statement and remove the last item.")
new_list2 = hex_digits
hex_digits.remove('f')
print(new_list2)

print("Associate the new list variable with the old list.")
new_list2 = new_list
print(new_list2)
