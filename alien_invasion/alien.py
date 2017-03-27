# alien_invasion
# alien
# AUTHOR: Maln
# TIME: 26/03/2017

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ A class to represent an alien"""

    def __init__(self, ai_settings, screen):
        """Initialize alien and set starting position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Load alien image and set rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near top left of screen
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        # Store alien'ss exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw alien at current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move alien right"""
        self.x+=(self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction)
        self.rect.x=self.x

    def check_edges(self):
        """Return true if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <=0:
            return True
