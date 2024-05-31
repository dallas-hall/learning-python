import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class to manage the player's ship"""

    def __init__(self, game):
        """Initialise the ship."""
        # Call the Sprite superclass constructor.
        super().__init__()
        # Load the game instance.
        self.screen = game.screen
        # Load the game's settings.
        self.settings = game.settings
        # Create a rectangle which will be our ship.
        self.screen_rect = game.screen.get_rect()
        # Load the ship image onto the rectangle.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        # Each new ship starts in the middle of the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        # Store the ship's exact horizontal position.
        self.x = float(self.rect.x)
        # Store the ship's exact vertical position.
        self.y = float(self.rect.y)
        # Movement flags, which are used to update the ships position when True.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Move the ship by 1 pixel if the directional movement flag is True."""
        # Stop the ship from moving off of the screen.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # Update the ship's position, not the rect. This is because we are using a float and rect's only support ints.
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        # Update the rect object with the new position. It will cast to an int and discard the decimal.
        self.rect.x = self.x
        self.rect.y = self.y

    def center_ship(self):
        """Reset the ship to its original position."""
        # Each new ship starts in the middle of the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        # Store the ship's exact horizontal position.
        self.x = float(self.rect.x)
        # Store the ship's exact vertical position.
        self.y = float(self.rect.y)

    def blit_me(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
