#!/usr/bin/python3

import logging, codecs, time

# Define logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - [%(levelname)s] - %(message)s')
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
logging.info('Starting BinaryReadingAndWriting.py')
logging.info('Reading file.')

with open('/home/dhall/tmp/brownfox', "rb") as binary_input_file, \
		open('/home/dhall/tmp/brownfox.bin', 'wb') as binary_output_file, \
		open('/home/dhall/tmp/brownfox.base64', 'wt') as base64_output_file:
	# Read the whole file at once
	binary_data = binary_input_file.read()

	if(debugging):
		logging.debug('Debug messages')
		time.sleep(.005)
		print(binary_data)
		print(binary_data.decode('utf-8'))
		# Encoding to base64 leaves it in binary mode, need to decode to text
		print(codecs.encode(binary_data, 'base64'))
		print(codecs.encode(binary_data, 'base64').decode('utf-8'))

	logging.info('Writing file.')
	binary_output_file.write(binary_data)
	base64_output_file.write(codecs.encode(binary_data, 'base64').decode('utf-8'))
