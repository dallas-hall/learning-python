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


# Using positional arguments. The order must be correct.
def positional_arguments(char, amount):
	"""Repeat a character n times."""
	print(f"{char}" * amount)


print('Using positional arguments.')
positional_arguments('a', 10)
# positional_arguments(10, 'b')  # This call will fail.


# Using keyword arguments. The order doesn't matter.
def keyword_arguments(char, amount):
	"""Repeat a character n times."""
	print(f"{char}" * amount)


print('Using keyword arguments.')
keyword_arguments(amount=10, char='b')
keyword_arguments(char='c', amount=10)
keyword_arguments('d', 10)  # Can still use positional arguments.


# The arguments without default values must be on the left so positional arguments still work.
def default_argument_value(char, amount=3):
	"""Repeat a character n times."""
	print(f"{char}" * amount)


# Multiple ways to call the same function.
print('Using default arguments values.')
default_argument_value('e')
default_argument_value('f', 10)  # Can still use positional arguments.
default_argument_value(char='g', amount=10)  # Can still use keyword arguments.


# The 3 functions above can be combined into a single function and called the same way.
def arguments(char, amount=3):
	"""Repeat a character n times."""
	print(f"{char}" * amount)


print('Using all 3 in one single function.')
arguments('h')
arguments('i', 10)
arguments(amount=10, char='j')
