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

people = {
	1: {
		'first_name': 'james',
		'last_name': 'jones',
		'age': 22,
		'height': 180,
		'weight': 70
	},
	2: {
		'first_name': 'jane',
		'last_name': 'jones',
		'age': 22,
		'height': 160,
		'weight': 45
	}
}

print(people.get(1))
print(people.get(2))

# Get a list of all the keys only
for key in people.keys():
	print("Printing key " + str(key))

# Does the same thing, implicit call to .keys()
for key in people:
	print("Printing key " + str(key))

# Get a list of all the values only
for value in people.values():
	print("Printing value " + str(value))

# Get a list of all the key and value pairs
for key, value in people.items():
	print("Printing key " + str(key) + ", which contains " + str(value))

for key in people:
	print("Key " + str(key))
	print("First Name: " + people.get(key).get('first_name'))
	print("Last Name: " + people.get(key).get('last_name'))
	print("Age: " + str(people.get(key).get('age')))
	print("Height: " + str(people.get(key).get('height')))
	print("Weight: " + str(people.get(key).get('weight')))