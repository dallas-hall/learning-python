#!/usr/bin/env python3
import logging
import os
import sys
import time

import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from scoreboard import Scoreboard

# Define logging output
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - [%(levelname)s] - %(message)s"
)

# Enable debugging messages
debugging = True
if not debugging:
    logging.disable(logging.DEBUG)
# Print start message and delay slightly
logging.info("Starting " + os.path.relpath(sys.argv[0]))
time.sleep(0.100)


class AlienInvasion:
    """Main class to manage the game assets and behaviour"""

    def __init__(self):
        """Initialise the game and create its resources"""
        # Create a flag to start and stop the game.
        self.game_active = False
        # Create a display window.
        pygame.init()
        # Create a game clock which is used to control frame rate.
        # If the game loop processes faster than this clock rate, we will slow it down so it is consistent.
        self.clock = pygame.time.Clock()
        # Create the game settings object which centrally stores the game's settigns.
        self.settings = Settings()
        # Change the screen dimensions of the entire game window.
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        # Full screen mode
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_width()
        # self.settings.screen_height = self.screen.get_height()

        # Create the game stats
        self.stats = GameStats(self)

        # Create the scoreboard
        self.scoreboard = Scoreboard(self)

        # Change the window caption
        pygame.display.set_caption("Alien Invasion")
        # Change the background colour.
        self.bg_color = self.settings.bg_color
        # Create the player's ship. Pass in the game instance via self.
        self.ship = Ship(self)
        # Create a group to control all bullets on the screen.
        self.bullets = pygame.sprite.Group()
        # Create a group to control all aliens on the screen.
        self.aliens = pygame.sprite.Group()
        self._create_alien_fleet()

        # Create the play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                # Update all active player bullets at once.
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            # Run the loop n times per second. e.g. if 60 then 60 frames per second.
            self.clock.tick(self.settings.fps)

    def _check_events(self):
        """Respond to keypress and mouse events."""
        for event in pygame.event.get():
            # Close the game via the window UI.
            if event.type == pygame.QUIT:
                sys.exit()
            # Handle a single key press, staring as the key goes down.
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # Handle holding a key, stopping as the key is released.
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            # Handle clicking the button
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the x,y coordinates of the mouse when it is clicked.
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_p:
            self._start_game()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        # Using multiple if statements will mean holding left and right at the same time has no movement.
        # The same applies to holding up and down at the same time.
        # But holding left or right and up or down at the same time allows diagonal movement.
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Shoot a bullet and add it to the bullet Sprite group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update bullet positions."""
        self.bullets.update()
        # Delete bullets that are no longer on the screen.
        # Python excepts the list to stay the same length while we are looping, so we need to work on a copy.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # Check if any bullets have collided with any aliens. If yes, remove the bullet and the alien.
        # The groupcollide function compares the rects of each group and looks for collisions.
        # The first 2 args are the groups to compare.
        # The second 2 args tell the function if to delete the collided objects.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.scoreboard.prep_score()
            self.scoreboard.check_high_scores()

        # Create a new alien fleet if all are shot down.
        if not self.aliens:
            self._create_alien_fleet()
            # Speed up the game during the next round.
            self.settings.increase_speed()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Set the background colour in each redraw of the screen during each loop iteration.
        self.screen.fill(self.bg_color)
        # Draw all player bullets.
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Draw the player's ship.
        self.ship.blit_me()
        # Draw the aliens via the Group draw method.
        self.aliens.draw(self.screen)
        # Draw the scoreboard
        self.scoreboard.show_score()
        # Draw the button if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()
        # Make the most recently drawn screen visible.
        # i.e. redraw the screen by discarding the old and creating the new.
        pygame.display.flip()

    def _create_alien_fleet(self):
        """Create the alien fleet."""
        # Create an alien object so we can get its size to use for spacing.
        alien = Alien(self)
        # The rect size contains a tuple of width and height.
        alien_width, alien_height = alien.rect.size
        # The position of the first alien is 1 alien width across from the edge of the screen and 1 alien height down.
        # Spacing between aliens is one alien width and one alien height.
        current_x, current_y = alien_width, alien_height
        # Keep creating aliens until there is no more room on the screen.
        # Keep adding on the y axis until we reach screen height minus 3 alien's height.
        while current_y < (self.settings.screen_height - 3 * alien_height):
            # Keep adding on the x axis until we reach screen width minus 2 alien's width.
            while current_x < (self.settings.screen_width - 2 * alien_width):
                # Create an alien at the current position and set its position.
                self._create_alien(current_x, current_y)
                # Increment the position for the next possible alien.
                # First width moves past the current alien, and the second width adds space.
                current_x += 2 * alien_width

            # Finished 1 row of aliens.
            # Reset x so we place the alien on the new row in the same starting spot below the previous row.
            # Increment y so we place the alien on the new row below the previous row.
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the fleet."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        # Add the alien to the Group of aliens.
        self.aliens.add(new_alien)

    def _update_aliens(self):
        """Update the position of all the aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien and player ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens reaching the bottom of the screen.
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """React when the alien fleet hits the edge of the screen."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the fleet down and change direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        # Multiplying a positive by a negative becomes negative.
        # Multiplying a negative by a negative becomes positive.
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """React to the player's ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Remove a player life.
            self.stats.ships_left -= 1

            # Clear the screen
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and recentre the ship.
            self._create_alien_fleet()
            self.ship.center_ship()

            # Pause the game briefly
            time.sleep(0.5)
        else:
            # Stop the game and display the cursor again.
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Check if any aliens reached the bottom."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks a button."""
        # Check if the x,y coordinates of the mouse click is on the play button.
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        # Only reactive to the button click when the game is inactive.
        if button_clicked and not self.game_active:
            # Hide the mouse cursor during gameplay.
            pygame.mouse.set_visible(False)
            self._start_game()

    def _start_game(self):
        # Reset the game state and start the game.
        self.settings.initialise_dynamic_settings()
        self.stats.reset_stats()
        self.scoreboard.prep_score()
        self.bullets.empty()
        self.aliens.empty()
        self._create_alien_fleet()
        self.ship.center_ship()
        self.game_active = True


# If this program is run as the driver program, then launch the game.
# https://stackoverflow.com/a/419185
if __name__ == "__main__":
    # Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()
