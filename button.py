import pygame.font
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Button:

    def __init__(self, game: 'AlienInvasion', message):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()

        self.font = pygame.font.Font(self.settings.font_file, 
            self.settings.button_font_size)
        self.rect = pygame.Rect(0,0,self.settings.button_w,self.settings.button_h)
        self.rect.center = self.boundaries.center
        self._prep_message(message)


    def _prep_message(self, message):
        self.message_image = self.font.render(message, True, self.settings.text_color, None)
        self.message_image_rect = self.message_image.get_rect()
        self.message_image_rect.center = self.rect.center

    
    def draw(self):
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.message_image, self.message_image_rect)


    def check_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)