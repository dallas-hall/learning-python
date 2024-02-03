class Settings:
	"""A class to store all the settings for the game."""

	def __init__(self):
		"""Initialise the game's settings"""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		# Light gray
		self.bg_color = (230, 230, 230)
		self.window_caption = "Alien Invasion"
		# Game clock, i.e. target FPS.
		self.fps = 120
		# The player's ship movement speed in pixels.
		self.ship_speed = 2.5
		self.ship_limit = 3
		# Bullet settings.
		self.bullet_speed = 5
		self.bullet_width = 3
		self.bullet_height = 15
		# Dark gray.
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 6
		# Alien Settings
		self.alien_speed = 1.0
		self.fleet_drop_speed = 10
		# Fleet direction, positive = right and negative = left.
		self.fleet_direction = 1
