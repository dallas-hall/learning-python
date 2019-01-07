#!/usr/bin/python3

import logging, sys, os, time

# Define logging output
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly
logging.info('Starting ' + os.path.relpath(sys.argv[0]))

logging.debug('Opening Workbook.')
# https://openpyxl.readthedocs.io/en/stable/tutorial.html#loading-from-a-file
from openpyxl import load_workbook
workbook = load_workbook('../Examples/example.xlsx')

logging.debug('Printing Worksheet Names.')
time.sleep(.005)
print(workbook.sheetnames)
