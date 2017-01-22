# dataviz
# parse.py
# AUTHOR: Maln
# TIME: 21/01/2017

import csv

MY_FILE = "../data/sample_sfpd_incident_all.csv"

def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-line object."""

    # Open CSV File
    opened_file = open(raw_file)

    # Read CSV File
    csv_data = csv.reader(opened_file, delimiter = delimiter)

    # setup an empty list
    parsed_data = []

    # skip over first line of file for headers
    fields=csv_data.next()

    # Iterate over each row of csv file, zip together field -> value
    for row in csv_data:
        parsed_data.append(dict(zip(fields,row)))

    # Close CSV File
    opened_file.close()
    # Build a data structure to return parsed_data


    return parsed_data

def main():
    # Call our parse function and give it needed parameters

    new_data = parse(MY_FILE, ",")

    print(new_data)