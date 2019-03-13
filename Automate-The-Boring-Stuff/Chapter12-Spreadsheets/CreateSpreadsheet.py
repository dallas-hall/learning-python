#!/usr/bin/python3

import logging, time
import openpyxl
from pathlib import Path
from datetime import datetime


# Define logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - [%(levelname)s] - %(message)s')
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
logging.info('Starting CreateSpreadsheet.py')
start_time = datetime.now()
time.sleep(0.005)

# https://openpyxl.readthedocs.io/en/stable/tutorial.html#loading-from-a-file
workbook = openpyxl.Workbook()
logging.info('Display all worksheet names. They are stored a list.')
time.sleep(0.005)
print(workbook.sheetnames)

logging.info('Display currently active worksheet name. Stored as a string and the default is \'Sheet\'.')
time.sleep(0.005)
worksheet = workbook.active  # Default is 0
print(worksheet.title)

logging.info('Update current worksheet name.')
time.sleep(0.005)
worksheet.title = 'Sheet-One'
print(worksheet.title)

logging.info('Saving the spreadsheet. Will overwrite without warning')
time.sleep(0.005)
workbook.save(Path.cwd() / 'output' / 'new-spreadsheet.xlsx')

elapsed_time = datetime.now() - start_time
time.sleep(0.005)
logging.info('Script completed. The process took {} (hh:mm:ss.ms)'.format(elapsed_time))
