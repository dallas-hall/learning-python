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

path = Path('/ssd/Development/random-files-for-dev-io/python-crash-course-3e-chapter-10-path-write-example.txt')
# Write a single string to a file.
# write_text will create a file if it doesn't exist and automatically close the file.
path.write_text('I love programming.\n')
print(path.read_text())

# Add multiple lines to a string and write that string to a file.
contents = 'Oh when the Roar... go marching in.\n'
contents += 'Oh when the Roar go marching in.\n'
contents += 'I want to be in that number... when the Roar go marching in.\n'
contents += 'OH WHEN THE ROAR.\nOH WHEN THE ROAR!\n'
contents += 'GOES MARCHING IN.\nGOES MARCHING IN!\n'
contents += 'Oh when the Roar go marching in.\n'
contents += 'I want to be in that number, when the Roar goes marching in.'
# write_text will overwrite an existing file.
path.write_text(contents)
print(path.read_text())
