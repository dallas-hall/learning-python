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

# A set is a collection where everything must be unique.
print("Printing the original list.")
aList = [1, 1, 2, 3, 4, 5, 5, 5, 6]
print(aList)
print("Printing the original list as a set.")
aSet = set(aList)
print(aSet)

# Duplicate items are lost. Sets do not retain any specific order.
aSet2 = {'d', 'a', 'c', 'c', 'b'}
print(aSet2) # This could randomly be in order.
print(sorted(aSet2))
