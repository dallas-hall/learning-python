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

# Handle the exception object
try:
	print(5 / 0)
except ZeroDivisionError:
	print("Cannot divide by 0.")

# Handle the exception object, but fail silently
try:
	print(5 / 0)
except ZeroDivisionError:
	# This tells Python to fail silently
	pass

# Don't handle the exception object, program crash
print(5 / 0)
