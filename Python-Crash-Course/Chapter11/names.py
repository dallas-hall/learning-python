#!/usr/bin/python3
import logging, sys, os, time
# In PyCharm, right click > Mark Directory As ? Sources root
from formatted_names import get_formatted_name

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.001)

done = False
while not done:
	first = input("Enter your first name (mandatory): ")
	middle  = input("Enter your middle name (optional): ")
	last = input("Enter your last name (optional): ")
	print(get_formatted_name(first, middle, last))
	result = input("Enter another name? (y|n): ")
	if result.lower() == "n":
		done = True

