# dataviz
# map
# AUTHOR: Maln
# TIME: 21/02/2017

import geojson as g
import parse as p

def create_map(data_file):
    # Define type of GeoJson we're creating
    geo_map = {"type":"FeatureCollection"}

    # Define empty list to collect point to graph
    item_list=[]

    # Iterate over our data to create GeoJSON doc
    # using enumerate so we get line as well
    # as the index, which is line number
    for index, line in enumerate(data_file):

        # Skip any zero coordinates (throws off map)
        if line['X']=="0" or line['Y'] == "0":
            continue
        # Setup new dictionary for each iteration
        data = {}
        # Assign line items to appropriate GeoJSON fiellds
        data['type'] = 'Feature'
        data['id'] = index
        data['properties'] = {'title':line['Category'],
                              'description':line['Descript'],
                              'date':line['Date']}
        data['geometry']={'type':'Point',
                          'coordinates':(line['X'],line['Y'])}

        # Add data dictionary to item_list
        item_list.append(data)

    # For each point in item_list, add point to dict.
    # setdefault creates a key called 'features' that
    # has a value type of an empty list. With each iteration
    # We are appending our point to that list
    for point in item_list:
        geo_map.setdefault('features',[]).append(point)

    # Now that all data is parsed in GeoJSON write to a file so
    # we can upload to gist.github.com
    with open('file_sf.geojson','w') as f:
        f.write(geojson.dumps(geo_map))

def main():
    data= p.parse(p.MY_FILE,",")

    return create_map(data)

if __name__=="__main__":
    main()