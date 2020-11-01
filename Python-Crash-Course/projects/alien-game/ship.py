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
		# Movement flags
		self.moving_left = False
		self.moving_right = False
		self.moving_up = False
		self.moving_down = False

	def blit_me(self):
		"""Draw the ship at its current location"""
		self.screen.blit(self.image, self.rect)

	def update_position(self):
		"""Update the ship's position using a movement flag."""
		if self.moving_right:
			self.rect.x += 1
		elif self.moving_left:
			self.rect.x -= 1
		elif self.moving_up:
			self.rect.y -= 1
		elif self.moving_down:
			self.rect.y += 1