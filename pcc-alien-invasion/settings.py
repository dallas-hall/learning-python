class Settings:
    """A class to store all the settings for the game."""

    def __init__(self):
        """Initialise the game's static settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # Light gray
        self.window_caption = "Alien Invasion"
        # Game clock, i.e. target FPS.
        self.fps = 120
        self.ship_limit = 3
        self.bullet_color = (60, 60, 60)  # Dark gray.
        self.bullets_allowed = 6
        self.bullet_width = 3
        self.bullet_height = 15
        # Don't need to increase drop speed as when the aliens speed up
        # they will come down the screen faster anyway.
        self.fleet_drop_speed = 10
        # 1 = constant, 1.1 = 10%, 2 = double. etc.
        self.speedup_scale = 1.15
        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):
        """These settings change during the game."""
        # Movement speed in pixels.
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0
        # Fleet direction, positive = right and negative = left.
        self.fleet_direction = 1
        # Score settings.
        self.alien_points = 50

    def increase_speed(self):
        """Increase the game speed."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
