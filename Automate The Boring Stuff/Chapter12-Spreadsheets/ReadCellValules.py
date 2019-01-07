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

logging.debug('Opening Worksheet.')
# https://openpyxl.readthedocs.io/en/stable/usage.html#read-an-existing-workbook
#worksheet = workbook.active
worksheet = workbook['Sheet1']

logging.debug('Printing worksheet.')
time.sleep(.005)
# Dates are automatically interpreted and returned as a datetime rather than a string.
print('The value at ' + worksheet['A1'].coordinate + ' is')
print(worksheet['A1'].value)
print('The format at ' + str(worksheet['A1'].row) + str(worksheet['A1'].column) + ' is')
print(worksheet['A1'].number_format)
print()
print('The value at ' + worksheet['B1'].coordinate + ' is')
print(worksheet['B1'].value)
print('The format at ' + str(worksheet['B1'].row) + str(worksheet['B1'].column) + ' is')
print(worksheet['B1'].number_format)
print()
print('The value at ' + worksheet['C1'].coordinate + ' is')
print(worksheet['C1'].value)
print('The format at ' + str(worksheet['C1'].row) + str(worksheet['C1'].column) + ' is')
print(worksheet['C1'].number_format)


