# dataviz
# graph.py
# AUTHOR: Maln
# TIME: 27/01/2017

import matplotlib.pyplot as plt
import parse
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
    plt.clg()

def main():
    visualize_days()

if __name__=="__main__":
    main()