# alien_invasion
# game_functions
# AUTHOR: Maln
# TIME: 24/03/2017

import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien


def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    """Respond to key-presses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen,stats, ship,aliens, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Start a new game when player clicks Play"""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)

    if button_clicked and not stats.game_active:
        start_game(ai_settings, screen, stats, ship, aliens, bullets)


def start_game(ai_settings, screen, stats, ship, aliens, bullets):
    """Starts game"""
    if not stats.game_active:
        # Hide mouse cursor
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        # Empty list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def check_keydown_events(event, ai_settings, screen,stats, ship,aliens, bullets):
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
    elif event.key == pygame.K_p:
        # Play game function here
        start_game(ai_settings,screen,stats,ship,aliens,bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button):
    """Update images on screen and flip to new screen"""
    # Redraw screen during pass through the loop
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # Draw play button if game is inactive
    if not stats.game_active:
        play_button.draw_button()

    # Make most recently drawn screen visible
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """Update position of bullets and gets rid of old bullets"""
    # Update Bullet positions
    bullets.update()

    # Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # check for bullets that have hit aliens
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # destroy bullets, create new fleet
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


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


def check_fleet_edges(ai_settings, aliens):
    """Respond appropirately iif any aliens have reached edge"""

    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Drop entire fleet and change fleet direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """Check if fleet is at an edge, then udpate positions for all aliens in fleet"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    # Look for aliens hitting bottom of screen
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Respond to ship being hit by alien"""
    if stats.ships_left > 0:
        # Decrement ships left
        stats.ships_left -= 1

        # Empty List of aliens and bullets
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Pause
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """Check if any aliens have reached bottom of screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat same as if ship got hit
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break
