#!/usr/bin/python3
import logging, sys, os, time

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.001)

aliensList = []

# Start at 1, exclude 7
number = 1
for alien in range(1, 7):
	if number == 1:
		new_alien = {
			'colour': 'green',
			'points': 5,
			'speed': 'slow'
		}
		aliensList.append(new_alien)
		number += 1
	elif number == 2:
		new_alien = {
			'colour': 'yellow',
			'points': 10,
			'speed': 'medium'
		}
		number += 1
		aliensList.append(new_alien)
	else:
		new_alien = {
			'colour': 'red',
			'points': 15,
			'speed': 'fast'
		}
		number = 1
		aliensList.append(new_alien)

for i in range(len(aliensList)):
	print("Alien " + str(i) + " is:")
	print("Colour: " + aliensList[i].get('colour'))
	print("Points: " + str(aliensList[i].get('points')))
	print("Speed: " + aliensList[i].get('speed'))