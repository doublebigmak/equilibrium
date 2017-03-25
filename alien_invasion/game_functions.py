# alien_invasion
# game_functions
# AUTHOR: Maln
# TIME: 24/03/2017

import sys
import pygame

def check_events(ship):
    """Respond to key-presses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)

def check_keydown_events(event,ship):
    """RESPOND TO KEYPRESSES"""
    if event.key == pygame.K_RIGHT:
        # MOve ship right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """Update imagess on screen and flip to new screen"""
    # Redraw screen during pass through the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make most recently drawn screen visible
    pygame.display.flip()
