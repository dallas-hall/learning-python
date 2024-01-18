#!/usr/bin/env python3
import logging, sys, os, time
from pathlib import Path

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.100)

path = Path("/ssd/Development/random-files-for-dev-io/id_rsa")
# This will throw an exception which will be caught.
try:
	# Read the file as utf-8
	contents = path.read_text(encoding="utf-8")
except FileNotFoundError:
	print("LOL my rsa ssh key isn't in that folder dawg...")

# This will throw an exception which will cause the crash.
contents = path.read_text(encoding="utf-8")
