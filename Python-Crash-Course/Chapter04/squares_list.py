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

# 1 to 10, exclude 11
squares = []
for i in range(1, 11):
	# i to the power of 2
	square = i ** 2
	squares.append(square)

print("The square values from 1 to 10.")
print(squares)

print("List comprehension - combining for loops and element creation into one line.")
squares = [i ** 2 for i in range(1, 11)]
print(squares)
