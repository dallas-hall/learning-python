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
time.sleep(.003)


# Using positional arguments. The order must be correct.
def positional_arguments(char, amount):
	"""Repeat a character n times."""
	print(f"{char}" * amount)


logging.info('Using positional arguments.')
time.sleep(.003)
positional_arguments('a', 10)
# This call would fail
# positional_arguments(10, 'b')


# Using keyword arguments. The order doesn't matter.
def keyword_arguments(char, amount):
	"""Repeat a character n times."""
	print(f"{char}" * amount)


logging.info('Using keyword arguments.')
time.sleep(.003)
keyword_arguments(amount=10, char='b')
keyword_arguments(char='c', amount=10)


# The arguments without default values must be on the left.
def default_argument_value(char, amount=3):
	"""Repeat a character n times."""
	print(f"{char}" * amount)


logging.info('Using default arguments values.')
time.sleep(.003)
# Multiple ways to call the same function
default_argument_value('d')
default_argument_value('e', 10)
default_argument_value(char='f', amount=10)

