# alien_invasion
# alien_invasion
# AUTHOR: Maln
# TIME: 21/03/2017

import sys

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # Initialize game and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in
    bullets = Group()

    # Start main loop
    while True:
        # Watch for keyboard and mouse events
        gf.check_events(ai_settings,screen,ship,bullets)

        ship.update()
        bullets.update()
        #Get rid of bullets
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))
        # Redraw screen during each pass through loop
        gf.update_screen(ai_settings, screen, ship,bullets)



run_game()
