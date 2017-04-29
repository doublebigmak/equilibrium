# alien_invasion
# ship
# AUTHOR: Maln
# TIME: 21/03/2017

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """Initialize ship and set starting position"""
        super(Ship,self).__init__()
        self.screen = screen

        # Load ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings


        # Start each new ship at bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        # Movement Flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ship's position based on movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center ship on screen"""
        self.center = self.screen_rect.centerx
