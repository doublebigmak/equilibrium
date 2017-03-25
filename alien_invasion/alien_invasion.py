# alien_invasion
# alien_invasion
# AUTHOR: Maln
# TIME: 21/03/2017

import sys

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize game and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(ai_settings, screen)

    # Start main loop
    while True:
        # Watch for keyboard and mouse events
        gf.check_events(ship)
        ship.update()
        # Redraw screen during each pass through loop
        gf.update_screen(ai_settings, screen, ship)



run_game()
