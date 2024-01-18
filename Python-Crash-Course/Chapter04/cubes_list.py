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

# 1 to 10, exclude 11
cubes = []
for i in range(1, 11):
	# i to the power of 3
	cubes.append(i ** 3)

print("The cubed values from 1 to 10.")
print(cubes)

print("List comprehension - combining for loops and element creation into one line.")
cubes = [i ** 3 for i in range(1, 11)]
print(cubes)
