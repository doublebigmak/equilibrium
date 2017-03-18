# test
# random_walk
# AUTHOR: Maln
# TIME: 07/03/2017

from random import choice


def get_step():
    """ Decide which direction to go and how far to go in that direction"""
    direction = choice([1,-1])
    distance = choice([0,1,2,3,4])
    step = direction*distance

    return step


class RandomWalk():
    """A class to generate random walks"""


    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0,0)
        self.x_values =[0]
        self.y_values =[0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until wallk reaches desired lengthh
        while len(self.x_values) < self.num_points:

            # Decide which direction to go and how far to go in that direction
            x_step = get_step()
            y_step = get_step()

            # Reject moves that go nowhere.
            if x_step==0 and y_step==0:
                continue

            # Calculate next x and y values.
            next_x = self.x_values[-1]+x_step
            next_y = self.y_values[-1]+y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
