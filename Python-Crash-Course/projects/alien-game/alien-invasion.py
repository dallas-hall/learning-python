#!/usr/bin/python3
import logging
import os
import sys
import time

import pygame

# Import from settings.py the class Settings
from settings import Settings
# Import the player's ship
from ship import Ship

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
		# Create a settings object from our Settings class
		self.settings = Settings()
		# Change the screen dimensions
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height)
		)
		# Change the window caption
		pygame.display.set_caption(self.settings.window_caption)
		# Change the screen from default black
		self.bg_color = (self.settings.bg_color)

		# Add the player's ship and pass in the current game instance
		self.ship = Ship(self)

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			self._check_events()
			self.ship.update_position()
			self._update_screen()

	def _check_events(self):
		"""Respond to player driven events."""
		# Watch for keyboard and mouse events.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			# Key pressed down
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					self.ship.moving_right = True
				if event.key == pygame.K_LEFT:
					self.ship.moving_left = True
				if event.key == pygame.K_UP:
					self.ship.moving_up = True
				if event.key == pygame.K_DOWN:
					self.ship.moving_down = True
			# Key released
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					self.ship.moving_right = False
				if event.key == pygame.K_LEFT:
					self.ship.moving_left = False
				if event.key == pygame.K_UP:
					self.ship.moving_up = False
				if event.key == pygame.K_DOWN:
					self.ship.moving_down = False

	def _update_screen(self):
		"""Update images on the screen."""
		# Redraw the screen during each pass through the loop, changing the colour
		self.screen.fill(self.bg_color)

		# Draw the player's ship ontop of the filled background
		self.ship.blit_me()

		# Make the most recently drawn screen visible
		pygame.display.flip()


# If this program is run as the driver program, then launch the game.
# https://stackoverflow.com/a/419185
if __name__ == '__main__':
	# Make a game instance and run the game.
	ai = AlienInvasion()
	ai.run_game()
