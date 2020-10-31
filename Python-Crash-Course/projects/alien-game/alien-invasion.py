#!/usr/bin/python3
import logging
import os
import sys
import time

import pygame

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.001)


class AlienInvasion:
	"""Main class to to manage the game assets and behaviour"""

	def __init__(self):
		"""Initialise the game and its resources"""
		pygame.init()
		self.screen = pygame.display.set_mode((1200, 800))
		pygame.display.set_caption("Alien Invasion")

		# Change the screen from default black
		self.bg_color = (230, 230, 230)

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			# Watch for keyboard and mouse events.
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			# Redraw the screen during each pass through the loop, changing the colour
			self.screen.fill(self.bg_color)

			# Make the most recently drawn screen visible
			pygame.display.flip()


# If this program is run as the driver program, then launch the game.
# https://stackoverflow.com/a/419185
if __name__ == '__main__':
	# Make a game instance and run the game.
	ai = AlienInvasion()
	ai.run_game()
