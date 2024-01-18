#!/usr/bin/env python3
import logging, sys, os, time
# To import this in PyCharm, right click the folder and mark as Sources Root
from dice import Dice

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.100)

dice_6_sides = Dice(6)
dice_10_sides = Dice(10)
dice_20_sides = Dice(20)
roll_amount = 5

print('Rolling ' + str(dice_6_sides.get_sides()) + ' sided dice ' + str(roll_amount) + ' times.')
for i in range(5):
	print(dice_6_sides.roll_dice())

print('Rolling ' + str(dice_10_sides.get_sides()) + ' sided dice ' + str(roll_amount) + ' times.')
for i in range(5):
	print(dice_10_sides.roll_dice())

print('Rolling ' + str(dice_20_sides.get_sides()) + ' sided dice ' + str(roll_amount) + ' times.')
for i in range(5):
	print(dice_20_sides.roll_dice())
