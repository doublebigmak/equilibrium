# test
# rw_visual.py
# AUTHOR: Maln
# TIME: 07/03/2017
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# make a random walk, plot points

rw = RandomWalk()
rw.fill_walk()

plt.scatter(rw.x_values,rw.y_values, s=15)

plt.show()