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
time.sleep(.001)

print("Dictionaries are Python's map data structures.")
dictionary = {}
print("Printing an empty dictionary")
print(dictionary)

# Adding key-value pairs.
dictionary['key1'] = "The first value in the map."
dictionary['key2'] = "The second value in the map."
print("'key1' points to " + str(dictionary['key1']))
print("'key2' points to " + str(dictionary['key2']))

# Modifying an existing key value pair
dictionary['key1'] = "The first value in the map (UPDATED)."
print(dictionary['key1'])

# Deleting an existing key value pair
del(dictionary['key1'])
# This will fail because we deleted it.
print(dictionary['key1'])