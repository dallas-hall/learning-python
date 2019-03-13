#!/usr/bin/python3

import logging, codecs, time

# Define logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - [%(levelname)s] - %(message)s')
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
logging.info('Starting Base64ToFile.py')
logging.info('Reading file.')

absolute_input_path = '/home/dhall/tmp/sunset.base64'
absolute_output_path = '/home/dhall/tmp/sunset_from_base64.jpg'

with open(absolute_input_path, "rt") as base64_input_file, \
		open(absolute_output_path, 'wb') as binary_output_file:
	base64_string = base64_input_file.read()
	# Decoding base64 string to binary after encoding the binary to text
	binary_data = codecs.decode(base64_string.encode('utf-8'), 'base64')
	if(debugging):
		logging.debug('Debug messages')
		time.sleep(.005)
		print(base64_string)
		print(binary_data)

	logging.info('Writing file.')
	binary_output_file.write(binary_data)