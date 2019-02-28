#!/usr/bin/python3

import logging

# Define logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - [%(levelname)s] - %(message)s')
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
logging.info('Starting NestedDictionaries.py')

people = {
	1: {
		'Name': 'Alice',
		'Age': 30,
		'Interests': {
			'Hacking',
			'Cracking',
			'Cryptography'
		}
	},
	2: {
		'Name': 'Bob',
		'Age': 30,
		'Interests': {
			'Hacking',
			'Cracking'
		}
	}
}

for person_id, person_info in people.items():
	print('Person ID: ' + str(person_id))
	for data in person_info:
		if type(person_info[data]) is set:
			print('Interests:')
			for value in person_info[data]:
				print('\t' + value)
		else:
			print(data + ': ' + str(person_info[data]))