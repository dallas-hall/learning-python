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


def get_message():
	# A docstring describing what the function does and is used to create documentation.
	"""Return hello world like a boss."""
	return "Hello, world!"


# Print the string returned by the function.
print(f"{get_message()}")
