"""
File Name: hud.py
Author: Tyler D. Collins
Date: 4/26/2026

Purpose: The purpose of this file is to create the HUD class/module that 
formats, displays and updates game scores, current level, and lives remaining
in the AlienInvasion game.
"""

# Import Necessary Modules w/ workaround for circular imports
import pygame.font
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class HUD:
    """Facilitates the creation and maintenance of the AlienInvasion game HUD

    Args:
        game (AlienInvasion): Refers to the AlienInvasion game

    Attributes:
        settings (Settings): Module of predefined specifications used to create
            and format the HUD that informs the user of game statistics
        screen (Surface): The screen/window generated to display the game
        boundaries (Rect): Coordinates/dimensions of the game window boundaries
        game_stats (GameStats): Contains updated records of game stats
        font (Font): Font style used for HUD text
        padding (int): Buffer space between separate HUD objects
        life_image (Surface): Image of a single life/ship in player's reserves
        life_rect (Rect): Coordinates/dimensions of a life image on game screen
        score_image (Surface): Text 'image' of the active game's current score 
        score_rect (Rect): Coordinates/dimensions of the score image
        max_score_image (Surface): Text 'image' of the session's hi-score
        max_score_rect (Rect): Coordinates/dimensions of the max score image
        hi_score_image (Surface): Text 'image' of the all-time hi-score
        hi_score_rect (Rect): Coordinates/dimensions of the hi-score image
        level_image (Surface): Text 'image' of the game's current level
        level_rect (Rect): Coordinates/dimensions of the level image
    """
    def __init__(self, game: 'AlienInvasion'):
        # Initialize attributes from AlienInvasion
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.game_stats = game.game_stats

        # Initialize HUD text font and boundary spacing
        self.font = pygame.font.Font(self.settings.font_file, 
            self.settings.HUD_font_size)
        self.padding: int = 20

        # Update HUD
        self.update_scores()
        self._setup_life_image()
        self.update_level()


    def _setup_life_image(self):
        """Loads and scales the image of a ship/life to display on HUD"""
        self.life_image = pygame.image.load(self.settings.ship_file)
        self.life_image = pygame.transform.scale(self.life_image, (
            self.settings.ship_w, self.settings.ship_h
            ))
        self.life_rect = self.life_image.get_rect()


    def update_scores(self):
        """Updates the on-screen display of game score(s)"""
        self._update_max_score()
        self._update_score()
        self._update_hi_score()


    def _update_score(self):
        """Displays a live-updated score counter of the active game score"""
        # Format display of score text
        score_str = f'Score: {self.game_stats.score: ,.0f}'
        self.score_image = self.font.render(score_str, True, 
            self.settings.text_color, None)
        
        # Place at top right of screen below max score
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.boundaries.right - self.padding
        self.score_rect.top = self.max_score_rect.bottom + self.padding


    def _update_max_score(self):
        """Displays a live-updated score counter of the hi-score of the current 
        game session
        """
        # Format display of max session score text
        max_score_str = f'Max Score: {self.game_stats.max_score: ,.0f}'
        self.max_score_image = self.font.render(max_score_str, True, 
            self.settings.text_color, None)
        
        # Place at top right corner of game screen
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.right = self.boundaries.right - self.padding
        self.max_score_rect.top = self.padding


    def _update_hi_score(self):
        """Displays a live-updated score counter of the all-time local 
        hi-score
        """
        # Format display of all-time local hi-score text
        hi_score_str = f'Hi-Score: {self.game_stats.hi_score: ,.0f}'
        self.hi_score_image = self.font.render(hi_score_str, True, 
            self.settings.text_color, None)
        
        # Place at top-middle of game screen
        self.hi_score_rect = self.hi_score_image.get_rect()
        self.hi_score_rect.midtop = (self.boundaries.centerx, self.padding)


    def update_level(self):
        """Displays an updated label of the current level of the active game"""
        # Format display of level text
        level_str = f'Level: {self.game_stats.level: ,.0f}'
        self.level_image = self.font.render(level_str, True, 
            self.settings.text_color, None)
        
        # Place at top left corner of game screen below lives remaining
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.padding
        self.level_rect.top = self.life_rect.bottom + self.padding


    def _draw_lives(self):
        """Displays images of the ship that represent the number of lives the 
        player has remaining in the active game
        """
        # Place at top left corner of game screen
        current_x = self.padding
        current_y = self.padding

        # Update to represent current number of lives remaining
        for _ in range(self.game_stats.ships_left):
            self.screen.blit(self.life_image, (current_x, current_y))
            current_x += self.life_rect.width + self.padding


    def draw(self):
        """Draws live score counters, current level and lives remaining to HUD 
        overlay on game screen
        """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.max_score_image, self.max_score_rect)
        self.screen.blit(self.hi_score_image, self.hi_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self._draw_lives()