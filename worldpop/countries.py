# worldpop
# countries.py
# AUTHOR: Maln
# TIME: 18/03/2017

from pygal.maps.world import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
