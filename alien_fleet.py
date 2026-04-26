"""
File Name: alien_fleet.py
Author: Tyler D. Collins
Date: 4/26/2026

Purpose: The purpose of this file is to create the AlienFleet class/module that
defines how the alien fleet structure is generated and facilitates collision 
behavior with other objects in the game.
"""

# Import Necessary Modules w/ workaround for circular imports
import pygame
from typing import TYPE_CHECKING
from alien import Alien
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class AlienFleet:
    """Represents the structure of the alien fleet in the AlienInvasion game

    Args:
        game (AlienInvasion): Refers to the AlienInvasion game

    Attributes
        settings (Settings): Module of predefined specifications used to create 
            the aliens within the fleet
        fleet (Group): Manages group of alien sprites that make up the entire 
            alien fleet
        fleet_direction (int): Variable acting as the 'switch' that determines 
            whether the alien fleet is moving left or right on-screen
        fleet_shift_speed (int): The relative distance the alien fleet shifts
            towards the ship/player when the alien fleet hits a boundary and 
            flips movement direction
    """
    def __init__(self, game: 'AlienInvasion'):
        # Initialize attributes from AlienInvasion
        self.game = game
        self.settings = game.settings

        # Create fleet sprite group
        self.fleet = pygame.sprite.Group()

        # Obtain fleet movement direction and shift speed from settings
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        # Generate alien fleet by adding new alien objects to fleet Sprite Group
        self.create_fleet()


    def create_fleet(self):
        """Constructs a new, full alien fleet on screen"""
        # Obtain screen and alien dimensions from settings
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        # Call methods that facilitate the construction of the alien fleet
        fleet_w, fleet_h = self.calculate_fleet_size(alien_w, screen_w, 
            alien_h, screen_h)
        x_offset, y_offset = self.calculate_offsets(alien_w, alien_h, 
            screen_w, fleet_w, fleet_h)
        self._create_rectangle_fleet(alien_w, alien_h, fleet_w, fleet_h, 
            x_offset, y_offset)


    def _create_rectangle_fleet(self, alien_w: int, alien_h: int, fleet_w: int, 
        fleet_h: int, x_offset: int, y_offset: int):
        """Facilitates filling out the rectangular structure of the alien fleet

        Args:
            alien_w (int): width of an alien sprite
            alien_h (int): height of an alien sprite
            fleet_w (int): # of aliens that can fit in a row of the fleet
            fleet_h (int): # of aliens that can fit in a column of the fleet
            x_offset (int): horizontal spacing between alien spaces
            y_offset (int): vertical spacing between alien spaces
        """
        # Create new aliens that form an array/fleet of aliens
        for row in range(fleet_h):
            for col in range(fleet_w):
                current_x = (alien_w * col) + x_offset
                current_y = (alien_h * row) + y_offset

                # Remove aliens in even rows & columns, adding spaces between 
                # aliens of the same row or column
                if col % 2 == 0 or row % 2 == 0:
                    continue
                self._create_alien(current_x, current_y)


    def calculate_offsets(self, alien_w: int, alien_h: int, screen_w: int, 
        fleet_w: int, fleet_h: int):
        """Calculate spacing between places within fleet columns and rows

        Args:
            alien_w (int): width of an alien sprite
            alien_h (int): height of an alien sprite
            screen_w (int): width of the game screen
            fleet_w (int): # of aliens that can fit in a row of the fleet
            fleet_h (int): # of aliens that can fit in a column of the fleet

        Returns:
            x_offset, y_offset (tuple): horizontal spacing between alien spaces, 
                vertical spacing between alien spaces
        """
        # Calculate vertical and horizontal dimensions of space filled by fleet
        half_screen = self.settings.screen_h // 2
        fleet_horizontal_space = fleet_w * alien_w
        fleet_vertical_space = fleet_h * alien_h

        # Determine spacing between aliens in fleet rows and columns
        x_offset = int((screen_w - fleet_horizontal_space)//2)
        y_offset = int((half_screen - fleet_vertical_space)//2)

        return (x_offset, y_offset)


    def calculate_fleet_size(self, alien_w: int, screen_w: int, alien_h: int, 
        screen_h: int):
        """Ensure fleet columns and rows are filled with max number of aliens 
        for the allotted space for the alien fleet upon start of level

        Args:
            alien_w (int): width of an alien sprite
            screen_w (int): width of the game screen
            alien_h (int): height of an alien sprite
            screen_h (int): height of the game screen

        Returns:
            fleet_w, fleet_h (tuple): number of aliens that can fill a row, 
                number of aliens that can fill a column
        """
        fleet_w = (screen_w // alien_w)
        fleet_h = ((screen_h / 2)//alien_h)

        # Find max # of aliens to fit in fleet rows
        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2

        # Find max # of aliens to fit in fleet columns
        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2

        return int(fleet_w), int(fleet_h)
    

    def _create_alien(self, current_x: int, current_y: int):
        """Add all newly created aliens to the fleet Sprite Group

        Args:
            current_x (int): screen 'x' coordinate of the next alien to be 
                added to the fleet
            current_y (int): screen 'y' coordinate of the next alien to be 
                added to the fleet
        """
        new_alien = Alien(self, current_x, current_y)
        self.fleet.add(new_alien)


    def _check_fleet_edges(self):
        """Flip direction of alien movement when screen boundary is reached"""
        alien: 'Alien'
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break


    def _drop_alien_fleet(self):
        """Drop alien fleet closer to ship when screen boundary is reached"""
        for alien in self.fleet:
            alien.y += self.fleet_drop_speed


    def update_fleet(self):
        """Updates fleet position and movement"""
        self._check_fleet_edges()
        self.fleet.update()

    def draw(self):
        """Draw an alien object to game screen for each alien in the fleet"""
        alien: 'Alien'
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group):
        """Checks for collisions between laser and alien sprites, removing 
        those that have collided from their respective groups

        Args:
            other_group (Group): Arsenal sprite group

        Returns:
            dict: A dictionary containing keys of alien sprites within the fleet
                that have collided with laser sprites, with their values as 
                lists of the laser sprites that collided with the alien
        """
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)


    def check_fleet_bottom(self):
        """Checks whether alien fleet has reached the bottom edge of screen 
        behind the ship

        Returns:
            bool: True if fleet has reached bottom edge of screen, 
                otherwise False
        """
        alien: 'Alien'
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_h:
                return True
        return False


    def check_destroyed_status(self):
        """Checks if entire alien fleet has been destroyed

        Returns:
            bool: False signifies the fleet still exists, True means fleet has 
                been destroyed
        """
        return not self.fleet