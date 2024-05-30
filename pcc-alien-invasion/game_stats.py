class GameStats:
    """Track game statistics."""

    def __init__(self, game):
        """Initialise game stats."""
        self.settings = game.settings
        self.reset_stats()

    def reset_stats(self):
        """Reset the game stats."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
