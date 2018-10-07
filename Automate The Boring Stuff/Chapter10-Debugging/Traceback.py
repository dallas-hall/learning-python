#!/usr/bin/python3

import logging, traceback, traceback2,time

# Define logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - [%(levelname)s] - %(message)s')
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
logging.info('Starting Traceback.py')
try:
	raise Exception('Error!')
except Exception as e:
	logging.debug('Traceback')
	print(traceback.format_exc())
	time.sleep(1)
	logging.debug('Traceback2')
	print(traceback2.format_exc())

print('Program running after the traceback and exception being handled.')