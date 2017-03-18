# test
# rw_visual.py
# AUTHOR: Maln
# TIME: 07/03/2017
import pygal

from random_walk import RandomWalk
# Keep making new walks as long as program is active
while True:
    # make a random walk, plot points
    rw = RandomWalk(5000)
    rw.fill_walk()

    chart = pygal.XY(stroke=False)
    chart.title= 'Random Walk'

    # Turn x and y values into tuples for points
    points = []
    for i in range(5000):
        point = (rw.x_values[i], rw.y_values[i])
        points.append(point)

    chart.add('A', points, dots_size = 4)
    chart.render_to_file('scatter.svg')

    keep_running = input("Make another walk? (y/n): ")
    if keep_running =='n':
        break
