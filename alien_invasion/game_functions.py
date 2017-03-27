# alien_invasion
# game_functions
# AUTHOR: Maln
# TIME: 24/03/2017

import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_events(ai_settings, screen, ship, bullets):
    """Respond to key-presses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """RESPOND TO KEYPRESSES"""
    if event.key == pygame.K_RIGHT:
        # MOve ship right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Create new bullet and add to bullets group
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Update images on screen and flip to new screen"""
    # Redraw screen during pass through the loop
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # Make most recently drawn screen visible
    pygame.display.flip()


def update_bullets(ai_settings,screen,ship,aliens, bullets):
    """Update position of bullets and gets rid of old bullets"""
    # Update Bullet positions
    bullets.update()

    # Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #check for bullets that have hit aliens
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)

    if len(aliens) == 0:
        # destroy bullets, create new fleet
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
    """FIRE a new bullet if limit not reached"""
    # create a new bullet and add to bulletss group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, ship, aliens):
    """create full fleet of aliens"""
    # Create alien and find number of aliens in a row
    # Spacing between alien is equal to one alien width
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Create fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    """Determine number of alienss that fit in a row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place in row"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.x = alien.x
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine number of rows of aliens that fit on screen"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def update_aliens(aliens):
    """Update positions of all aliens in fleet"""
    aliens.update()

def check_fleet_edges(ai_settings, aliens):
    """Respond appropirately iif any aliens have reached edge"""

    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    """Drop entire fleet and change fleet direction"""
    for alien in aliens.sprites():
        alien.rect.y+=ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings,aliens):
    """Check if fleet is at an edge, then udpate positions for all aliens in fleet"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

