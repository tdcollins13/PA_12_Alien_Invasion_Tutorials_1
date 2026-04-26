"""
File Name: alien.py
Author: Tyler D. Collins
Date: 4/26/2026

Purpose: The purpose of this file is to creat the Alien class/module that 
defines how the aliens in the alien fleet are generated, their position and 
their movement behavior.
"""

# Import Necessary Modules w/ workaround for circular imports
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_fleet import AlienFleet


class Alien(Sprite):
    """Represents a single alien sprite in the AlienInvasion game

    Args:
        fleet (AlienFleet): The complete structure of enemy alien sprites
        x (float): screen 'x' coordinate of the next alien to be added to the 
            fleet
        y (float): screen 'y' coordinate of the next alien to be added to the 
            fleet

    Attributes:
        fleet (AlienFleet): Represents the entire alien fleet
        screen (Surface): The image/space of the game screen
        boundaries (Rect): Coordinates/dimensions of the game screen boundaries
        settings (Settings): Module of predefined specifications used to create 
            the alien(s)
        image (Surface): The on-screen image of an individual alien
        rect (Rect): Coordinates/dimensions of the alien image
        y (int): 'y' coordinate on game screen of top left corner of alien
        x (int): 'x' coordinate on game screen of top left corner of alien
    """
    def __init__(self, fleet: 'AlienFleet', x: float, y: float):
        # Initialize game attributes from AlienInvasion
        super().__init__()
        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings

        # Load and scale alien image
        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.alien_w, self.settings.alien_h)
            )
        
        # 'First' alien in alien fleet positioned at top of game screen's left 
        # edge at game start
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)


    def update(self):
        """Updating alien position and movement"""
        temp_speed = self.settings.fleet_speed
        self.x += temp_speed * self.fleet.fleet_direction
        self.rect.x = self.x
        self.rect.y = self.y


    def check_edges(self):
        """Determine if alien has reached the left or right boundary of screen

        Returns:
            bool: False if no aliens are in contact with screen boundaries, 
                True if alien(s) have reached a screen boundaries
        """
        return (self.rect.right >= self.boundaries.right or 
                self.rect.left <= self.boundaries.left)


    def draw_alien(self):
        """Draw alien image to game screen"""
        self.screen.blit(self.image, self.rect)