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
print('Changing key1.')
dictionary['key1'] = "The first value in the map (UPDATED)."
print(dictionary['key1'])

# Deleting an existing key value pair
print('Deleting key1 and then searching for it a few different ways.')
del(dictionary['key1'])
# Returns None when it doesn't exist
print(dictionary.get('key1'))
# Return what you want when it doesn't exist
print(dictionary.get('key1', 'Not Found.'))
# This will fail because we deleted it.
print(dictionary['key1'])
