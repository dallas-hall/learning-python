import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Bullets fired from the player's ship."""

    def __init__(self, game):
        """Create a bullet object at the ship's current position."""
        # Call the Sprite constructor so we can inherit from it.
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color
        # Create a bullet rect at 0,0 and set its correct position. Which is directly above the ship.
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        self.rect.midtop = game.ship.rect.midtop
        # Bullet speed
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the bullet's position. Decreasing y moves up the screen.
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet."""
        pygame.draw.rect(self.screen, self.color, self.rect)
