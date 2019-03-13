#!/usr/bin/python3

import logging, time, codecs

# Define logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - [%(levelname)s] - %(message)s')
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
logging.info('Starting FileToBase64.py')
logging.info('Reading file.')

absolute_input_path = '/home/dhall/tmp/sunset.jpg'
absolute_output_path = '/home/dhall/tmp/sunset.base64'

with open(absolute_input_path, "rb") as binary_input_file, \
		open(absolute_output_path, 'wt') as base64_output_file:
	binary_data = binary_input_file.read()
	if(debugging):
		logging.debug('Debug messages')
		time.sleep(.005)
		print(binary_data)
		# Encoding to base64 leaves it in binary mode, need to decode the binary text
		print(codecs.encode(binary_data, 'base64'))
		print(codecs.encode(binary_data, 'base64').decode('utf-8'))

	logging.info('Writing file.')
	base64_output_file.write(codecs.encode(binary_data, 'base64').decode('utf-8'))
