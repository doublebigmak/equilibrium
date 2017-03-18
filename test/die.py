# test
# die
# AUTHOR: Maln
# TIME: 10/03/2017

from random import randint

class Die():
    """A class representing a single die"""

    def __init__(self, num_sides = 6):
        """Assume a six-sided die"""
        self.num_sides = num_sides
        self.min_side = 1

    def roll(self):
        """Return a random value between 1 and number of slides"""
        return randint(1,self.num_sides)

