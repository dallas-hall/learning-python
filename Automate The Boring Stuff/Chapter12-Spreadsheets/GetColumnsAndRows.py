#!/usr/bin/python3

import logging, time
from openpyxl import load_workbook

# Define logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - [%(levelname)s] - %(message)s')
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
logging.info('Starting GetColumnsAndRows.py')

# https://openpyxl.readthedocs.io/en/stable/tutorial.html#loading-from-a-file
workbook = load_workbook('../Examples/example.xlsx')

logging.debug('Opening Worksheet.')
time.sleep(0.005)
# https://openpyxl.readthedocs.io/en/stable/usage.html#read-an-existing-workbook
#worksheet = workbook.active
worksheet = workbook['Sheet1']
if debugging:
	time.sleep(0.005)
	logging.info('The rows and cells returned are:')
	print(tuple(worksheet))

i = 1
# Use splices to get a rectangle of cells.
for row in worksheet['A1':'C3']:
	print('--- ROW ' + str(i) + ' ---')
	for cell in row:
		print(cell.coordinate, cell.value)
	print('--- END OF ROW ----')
	i += 1

time.sleep(0.003)
logging.info('Script completed.')