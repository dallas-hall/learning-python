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

path = Path('/ssd/Development/random-files-for-dev-io/UTF-8-demo.txt')
# read_text will return an empty string when it gets to the end of file.
# This will be displayed as a blank line. Use rstrip() to remove it.
contents = path.read_text().rstrip()
print(contents)

path = Path('/ssd/Development/random-files-for-dev-io/i-can-eat-glass.txt')
contents = path.read_text()
lines = contents.splitlines()
for line in lines:
    print(line)

# This is the same as above
for line in contents.splitlines():
    print(line)
