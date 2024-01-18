#!/usr/bin/env python3
import logging, sys, os, time

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.100)

aliensList = []

# Start at 1, exclude 4.
for alien in range(1, 4):
	new_alien = {
		'colour': 'green',
		'points': 5,
		'speed': 'slow'
	}
	aliensList.append(new_alien)

print('# Printing aliens.')
for i in range(len(aliensList)):
	print("Alien " + str(i) + " is:")
	print("Colour: " + aliensList[i].get('colour'))
	print("Points: " + str(aliensList[i].get('points')))
	print("Speed: " + aliensList[i].get('speed'))

# Update the last alien from green to yellow.
for alien in aliensList[-1:]:
	if alien['colour'] == 'green':
		alien['colour'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10

print('\n# Printing aliens.')
for i in range(len(aliensList)):
	print("Alien " + str(i) + " is:")
	print("Colour: " + aliensList[i].get('colour'))
	print("Points: " + str(aliensList[i].get('points')))
	print("Speed: " + aliensList[i].get('speed'))

# Update the last 2 aliens from green to yellow or yellow to red..
for alien in aliensList[-2:]:
	if alien['colour'] == 'green':
		alien['colour'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['colour'] == 'yellow':
		alien['colour'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15

print('\n# Printing aliens.')
for i in range(len(aliensList)):
	print("Alien " + str(i) + " is:")
	print("Colour: " + aliensList[i].get('colour'))
	print("Points: " + str(aliensList[i].get('points')))
	print("Speed: " + aliensList[i].get('speed'))
