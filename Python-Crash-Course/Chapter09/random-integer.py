#!/usr/bin/python3
import logging, sys, os, time
from random import choice
from dice import Dice

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.001)

players = [
	"player1",
	"player2",
	"player3",
	"player4"
]

starting_player = choice(players)
print(f"The first player will be {starting_player}.")

di1 = Dice(6)
print(f"Rolling the {di1.get_sides()} side di.")
for i in range(1, 11):
	print(f"Roll {i} is {di1.roll_dice()}.")











