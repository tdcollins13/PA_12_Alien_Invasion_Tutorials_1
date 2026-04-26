"""
File Name: arsenal.py
Author: Tyler D. Collins
Date: 4/26/2026

Purpose: The purpose of this file is to create the Arsenal class/module that 
defines how the ammo capacity and expended ammo from the ship/player is 
managed.
"""

# Import Necessary Modules w/ workaround for circular imports
import pygame
from bullet import Bullet
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Arsenal:
    """Represents the ammo reserves of the ship/player in the AlienInvasion game

    Args:
        game (AlienInvasion): Refers to the AlienInvasion game

    Attributes:
        settings (Settings): Module of Predefined specifications used to create 
            ship's arsenal
        arsenal (Group): Manages group of bullet sprites for the ship to fire
    """
    def __init__(self, game: 'AlienInvasion'):
        # Initialize attributes from AlienInvasion
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()


    def update_arsenal(self):
        """Updates quantity of bullets in ship arsenal"""
        self.arsenal.update()
        self._remove_bullets_offscreen()


    def _remove_bullets_offscreen(self):
        """Make bullet available for re-fire once it leaves game screen"""
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)


    def draw(self):
        """Draw bullet image to game screen once fired"""
        for bullet in self.arsenal:
            bullet.draw_bullet()


    def fire_bullet(self):
        """Fires a new bullet/laser sprite. Bullets/Lasers are fired only when 
        there is ammo left in ship arsenal

        Returns:
            bool: True when a bullet is successfully fired, otherwise False
        """
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False