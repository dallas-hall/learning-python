import pygame


class Ship:
	"""A class to manage the player's ship"""

	def __init__(self, game):
		"""Initialise the ship."""
		self.screen = game.screen
		self.screen_rect = game.screen.get_rect()
		# Load the ship image
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		# Each new ship starts in the middle of the bottom of the screen
		self.rect.midbottom = self.screen_rect.midbottom

	def blit_me(self):
		"""Draw the ship at its current location"""
		self.screen.blit(self.image, self.rect)
