"""
File Name: settings.py
Author: Tyler D. Collins
Date: 4/26/2026

Purpose: The purpose of this file is to create the Settings class/module that 
contains a set of specifications to be used in the creation of the 
AlienInvasion game.
"""

# Import path library
from pathlib import Path


class Settings:
    """Represents the settings used in generating the AlienInvasion game

    Attributes:
        name (str): The name of the AlienInvasion game to appear on game window
        screen_w (int): The relative width of the game screen/window
        screen_h (int): The relative height of the game screen/window
        FPS (int): The speed at which new frames for the game are drawn, in 
            frames per second
        bg_file (Path): Path of the image file used as the background of the 
            game window

        ship_file (Path): Path of to the image file used as the ship/player
        ship_w (int): The relative width of the ship/player object on the game 
            screen
        ship_h (int): The relative height of the ship/player object on the game 
            screen
        starting_ship_count (int): The number of lives/ships the player has left

        bullet_file (Path): Path of the image file used as the bullets/
            lasers fired by the ship/player
        laser_sound (Path): Path of the audio file used for ship laser fire
        impact_sound (Path): Path of the audio file used for laser collisions 
            with aliens
        bullet_w (int): The relative width of the bullet/laser object on the 
            game screen
        bullet_h (int): The relative height of the bullet/laser object on the 
            game screen
        bullet_amount (int): The maximum number of bullets/lasers the 
            ship/player can have in their arsenal at any time

        alien_file (Path): Path of the image file used to depict an alien object
        alien_w (int): Refers to the relative width of an individual alien 
            object
        alien_h (int): Refers to the relative height of an individual alien 
            object

        button_w (int): The relative width of the play button on the game screen
        button_h (int): The relative height of the play button on the game scrn
        button_color (tuple): Contains 3 RGB values that create the specific 
            color of the play button

        text_color (tuple): Contains 3 RGB values that create the specific 
            color for the HUD and play button text
        button_font_size (int): The size of the font used for the play button
        HUD_font_size (int): The size of the font used for HUD features
        font_file (Path): Path of the ttf file that loads the font used for 
            HUD and button text

        scores_file (Path): Path of the json file that records hi-scores
        alien_points (int): Points awarded for every alien that is destroyed

        difficulty_scale (float): Scaling factor that increases game difficulty 
            when a new level begins
        ship_speed (int): The speed of the ship/player when moving horizontally
        bullet_speed (int): The speed of a bullet/laser when moving across the 
            screen
        fleet_speed (int): The speed of the alien fleet when moving on-screen
        fleet_direction (int): Variable acting as the 'switch' that determines 
            whether the alien fleet is moving left or right on-screen
        fleet_drop_speed (int): The relative distance the alien fleet drops
            towards the ship/player when the alien fleet hits a boundary and 
            flips movement direction
    """
    def __init__(self):
        # Game screen/window settings
        self.name: str = "Alien Invasion"
        self.screen_w: int = 1200
        self.screen_h: int = 600
        self.FPS: int = 60
        self.bg_file: Path = (Path.cwd() / 'Assets'/ 'images' / 
            'Starbasesnow.png')

        # Ship settings
        self.ship_file: Path = (Path.cwd() / 'Assets' / 'images' / 
            'ship2(no bg).png')
        self.ship_w: int = 40
        self.ship_h: int = 60

        # Bullet settings
        self.bullet_file: Path = (Path.cwd() / 'Assets' / 'images' / 
            'laserBlast.png')
        self.laser_sound: Path = (Path.cwd() / 'Assets' / 'sound' / 
            'laser.mp3')
        self.impact_sound: Path = (Path.cwd() / 'Assets' / 'sound' / 
            'impactSound.mp3')
        self.bullet_w: int = 25
        self.bullet_h: int = 80

        # Alien fleet settings
        self.alien_file: Path = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
        self.alien_w: int = 30
        self.alien_h: int = 30
        self.fleet_direction: int = 1
        self.fleet_drop_speed: int = 40

        # Button settings
        self.button_w: int = 200
        self.button_h: int = 50
        self.button_color: tuple = (194,2,2)

        # Font settings
        self.text_color: tuple = (255,255,255)
        self.button_font_size: int = 48
        self.HUD_font_size: int = 20
        self.font_file: Path = (Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen' /
            'Silkscreen-Bold.ttf')

        # Score & difficulty settings
        self.difficulty_scale: float = 1.1
        self.scores_file: Path = Path.cwd() / 'Assets' / 'file' / 'scores.json'
        self.alien_points: int = 50

    def initialize_dynamic_settings(self):
        """Initializes settings that have a direct impact on the difficulty of 
        gameplay
        """
        self.ship_speed: int = 5
        self.starting_ship_count: int = 3
        self.bullet_w: int = 25
        self.bullet_h: int = 80
        self.bullet_speed: int = 7
        self.bullet_amount: int = 5
        self.fleet_speed: int = 1
        self.fleet_drop_speed: int = 40
        self.alien_points: int = 50

    def increase_difficulty(self):
        """Increases the game's difficulty by changing the speeds of objects 
        during gameplay
        """
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale