# temperaturereader
# high_lows.py
# AUTHOR: Maln
# TIME: 18/03/2017

import csv

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)