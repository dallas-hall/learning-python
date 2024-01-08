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

# 1 to 10
for i in range(1, 11):
	if i % 2 == 0:
		print(f"Number {i} is even.")
	else:
		# Skip odd numbers.
		continue
