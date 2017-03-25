# alien_invasion
# ship
# AUTHOR: Maln
# TIME: 21/03/2017

import pygame

class Ship():

    def __init__(self, screen):
        """Initialize ship and set starting position"""
        self.screen = screen

        # Load ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)