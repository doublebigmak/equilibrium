# dataviz
# graph.py
# AUTHOR: Maln
# TIME: 27/01/2017

import matplotlib.pyplot as plt
import parse
import numpy as np
from collections import Counter


MY_FILE = "sample_sfpd_incident_all.csv"
def visualize_days():
    """Visualize data by day of week"""

    # grab parsed data that we parsed earlier
    data_file = parse.parse(MY_FILE, ",")

    # make a new variable, 'counter', from iterating through
    # each line of data in parsed data, and count how many incidents
    # happen on each day of the week
    counter = Counter(item["DayOfWeek"] for item in data_file)
    # separate the x-axis data (the days of the week) from the
    # counter variable from the y-axis data ( number of incidents for each day)
    data_list = [
                counter["Monday"],
                counter["Tuesday"],
                counter["Wednesday"],
                counter["Thursday"],
                counter["Friday"],
                counter["Saturday"],
                counter["Sunday"]
                ]
    day_tuple=tuple(["Mon","Tues","Wed","Thurs","Fri","Sat","Sun"])
    # with y-axis data, assign to matplotlib plot instance
    plt.plot(data_list)
    # create amount of ticks needed for x-axis, assign labes
    plt.xticks(range(len(day_tuple)),day_tuple)
    # save plot
    plt.savefig("Days.png")
    #close plot file
    plt.clf()

def visualize_type():
    """Visualize data by category in a bar graph"""

    # grab parsed data
    data_file = parse.parse(MY_FILE,",")
    # make a new variable, 'counter', from iterating through each line
    # of data in parsed data, and count how many incidents happen
    # by category
    counter = Counter(item["Category"]for item in data_file)

    # set labels which are based on keys of our counter
    # since order doesn't matter, can use counter.keys()
    labels = tuple(counter.keys())

    # Set exactly where labels hit x-axis
    xlocations = np.arange(len(labels))+0.5
    width = 0.5

    # assign data to a bar plot (similar to plt.plot())
    plt.bar(xlocations,counter.values(),width=width)

    # Assign labels and tick location to x-axis
    plt.xticks(xlocations+width/2,labels,rotation = 90)

    # Give some more room so the x-axis labels aren't cut off in graph
    plt.subplots_adjust(bottom=0.4)

    # Make the overall graph/figure larger
    plt.rcParams['figure.figsize'] = 12,8

    # Save the gprah
    plt.savefig("Type.png")

    # Close plot figure
    plt.clf()
def main():
    #visualize_days()
    visualize_type()

if __name__=="__main__":
    main()