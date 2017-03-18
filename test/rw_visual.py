# test
# rw_visual.py
# AUTHOR: Maln
# TIME: 07/03/2017
import matplotlib.pyplot as plt

from random_walk import RandomWalk
# Keep making new walks as long as program is active
while True:
    # make a random walk, plot points
    rw = RandomWalk(5000)
    rw.fill_walk()

    # set size of plotting window
    plt.figure(figsize=(12,8))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
    #plt.plot(rw.x_values,rw.y_values,c='grey',linewidth=1)
    # emphasize first and last points
    plt.scatter(0,0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)

    # remove the axis
    plt.xticks([])
    plt.yticks([])

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running =='n':
        break
