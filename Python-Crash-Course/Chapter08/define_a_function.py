#!/usr/bin/env python
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


def hello_world():
	# A docstring describing what the function does and is used to create documentation.
	"""Print hello world like a boss."""
	message = "Hello, world!"
	print(f"{message}")


# The variable msg is the function's parameter.
# Whatever value is passed into the function is the function's argument.
# These can be used interchangeably.
def print_message(msg):
	"""Prints whatever the user passed in."""
	print(f"{msg}")


hello_world()
print_message("Ahihihihi, Mr World.")
