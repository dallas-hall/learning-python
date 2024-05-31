import pygame.font


class Button:
    """Create a button for the game."""

    def __init__(self, game, msg):
        """Create a button."""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the button dimensions and properties.
        self.width, self.height = 200, 50
        # Dark Green
        self.button_color = (0, 135, 0)
        # White
        self.text_color = (255, 255, 255)
        # Use the default font at size 48.
        self.font = pygame.font.SysFont(None, 48)

        # Create the button with a Rect and centre it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Add the button message by rendering the text as an image.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn the message into a rendered image."""
        # Turn on antialiasing to make it easier to read.
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw the button and then the image."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
