import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
	"""A class to manage those pesky aliens."""

	def __init__(self, game):
		"""Initialise the aliens."""
		# Call the Sprite constructor so we have it's methods available.
		super().__init__()
		self.screen = game.screen
		self.settings = game.settings

		# Load the alien image and get its rect.
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		# Start each new alien near the top left of the screen.
		# Add space to the left of the alien and above the alien, so its easy to see.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store a float for the alien's exact horizontal position.
		self.x = float(self.rect.x)

	def check_edges(self):
		"""Return true if the alien is at the edge of the screen."""
		screen_rect = self.screen.get_rect()
		# Is the rect object at or beyond the right side of the screen, or
		# Is the rect object at or beyond the left side of the screen.
		return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

	def update(self):
		"""Move the alien to the right."""
		# If fleet direction is positive the aliens will move right, or
		# If fleet direction is negative the aliens will move left.
		self.x += self.settings.alien_speed * self.settings.fleet_direction
		self.rect.x = self.x
