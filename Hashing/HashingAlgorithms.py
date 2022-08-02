#!/usr/bin/python3
import logging, sys, os, time, hashlib, pprint

# Define logging output
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.002)
pp = pprint.PrettyPrinter()

logging.info('All available algorithms.')
time.sleep(.003)
print(pp.pprint(hashlib.algorithms_available))

logging.info('All algorithms guarenteed to work on this platform.')
time.sleep(.003)
print(pp.pprint(hashlib.algorithms_guaranteed))

