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

names = [
	["john"],
	["john", "jones"],
	["john", "jerry", "jones"]
]


# Default value of nothing or its overriden by the user
def print_name(first_name, last_name="", middle_name=""):
	if middle_name and last_name:
		formatted_full_name = f"{first_name} {middle_name} {last_name}"
	elif not middle_name and last_name:
		formatted_full_name = f"{first_name} {last_name}"
	else:
		formatted_full_name = f"{first_name}"
	return formatted_full_name.title()


for i in range(len(names)):
	if len(names[i]) == 1:
		full_name = print_name(names[i][0])
	elif len(names[i]) == 2:
		full_name = print_name(names[i][0], names[i][1])
	else:
		full_name = print_name(names[i][0], names[i][2], names[i][1])
	print(full_name)
