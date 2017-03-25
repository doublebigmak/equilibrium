# alien_invasion
# keys_test
# AUTHOR: Maln
# TIME: 24/03/2017

import pygame
import sys

from settings import Settings

def run_game():
    # Initialize game and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Keys Test")
    pygame.font.init()
    myfont = pygame.font.SysFont("monochrome",60)

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)
                label = myfont.render(str(event.key), 1, (0,0,0))
                screen.fill(ai_settings.bg_color)
                screen.blit(label, (0,0))
                pygame.display.flip()



run_game()
