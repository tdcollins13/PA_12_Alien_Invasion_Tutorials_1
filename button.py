"""
File Name: button.py
Author: Tyler D. Collins
Date: 4/26/2026

Purpose: The purpose of this file is to create the Button class/module that 
generates and formats a 'play' button at the beginning of a new game of 
AlienInvasion.
"""

# Import Necessary Modules w/ workaround for circular imports
import pygame.font
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Button:
    """Responsible for formatting and displaying a 'Play' button at the start 
    and end of the AlienInvasion game

    Args:
        game (AlienInvasion): Refers to the AlienInvasion game
        message (str): Text to be displayed on top of the game start button

    Attributes:
        settings (Settings): Module of predefined specifications used to format 
            and display the play button before a new game begins
        screen (Surface): The screen/window generated to display the game
        boundaries (Rect): Coordinates/dimensions of the game window boundaries
        font (Font): Font style used for button text
        rect (Rect): Coordinates/dimensions of the play button
        message_image (Surface): Text 'image' displayed on top of the play bttn
        message_image_rect (Rect): Coordinates/dimensions of text image on bttn
    """
    def __init__(self, game: 'AlienInvasion', message: str):
        # Initialize Attributes from AlienInvasion
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()

        # Format button size, font, position and appearance
        self.font = pygame.font.Font(self.settings.font_file, 
            self.settings.button_font_size)
        self.rect = pygame.Rect(0,0,self.settings.button_w,self.settings.button_h)
        self.rect.center = self.boundaries.center
        self._prep_message(message)


    def _prep_message(self, message):
        """Formats text overlay for the game start button

        Args:
            message (str): Text to be displayed on top of the game start button
        """
        self.message_image = self.font.render(message, True, 
            self.settings.text_color, None)
        self.message_image_rect = self.message_image.get_rect()
        self.message_image_rect.center = self.rect.center

    
    def draw(self):
        """Draws button image to game screen"""
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.message_image, self.message_image_rect)


    def check_clicked(self, mouse_pos):
        """Determines when the user clicks the game's play button

        Args:
            mouse_pos (Coordinate): Location of the user's mouse/cursor

        Returns:
            (bool): Evaluates True when user clicks play button, otherwise False
        """
        return bool(self.rect.collidepoint(mouse_pos))