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

numbers = [10, 20, 30, 40, 50]

print("Looping through a list.")
for number in numbers:
	print("The current number is " + str(number))

print("Looping through a number range, start at 0.")
# Starts at 0 and excludes 5
for i in range(5):
	print("i is currently " + str(i))
print("Looping through a number range, start at specified number.")
# Starts at 5 and excludes 10
for i in range(5, 10):
	print("i is currently " + str(i))

print("Make a list of numbers from a number range.")
# Creates a list from 1 to 4
number_range = list(range(1, 5))
print(number_range)

print("Looping through a number range, start at specified number, and increment by specified number.")
# Start at 2, increment by 2 and exclude 16.
for i in range(2, 16, 2):
	print("i is currently " + str(i))
