# alien_invasion
# settings
# AUTHOR: Maln
# TIME: 21/03/2017

class Settings():
    """Class to store all settings for game"""

    def __init__(self):
        """Initialize game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        # Set BG colour
        self.bg_color = (230,230,230)

        #Ship Settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 5

        # Alien Settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet direction 1 = right, -1 = left
        self.fleet_direction = 1


