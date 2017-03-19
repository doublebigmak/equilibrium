# worldpop
# country_codes
# AUTHOR: Maln
# TIME: 18/03/2017

from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Return Pygal 2-digit country code for given country"""

    for code, name in COUNTRIES.items():
        if name== country_name:
            return code
        elif country_name == 'Yemen, Rep.':
            return 'ye'
        elif country_name == 'Vietnam':
            return 'vn'
        elif country_name == 'Venezuela, RB':
            return 've'
        elif country_name == 'Tanzania':
            return 'tz'
        elif country_name == 'Taiwan':
            return 'tw'
        elif country_name == 'Macedonia, FYR':
            return 'mk'
        elif country_name == 'Moldova':
            return 'md'
        elif country_name == 'Libya':
            return 'lb'
        elif country_name == 'Lao PDR':
            return 'la'
        elif country_name == 'Slovak Republic':
            return 'sk'
        elif country_name == 'Korea, Dem. Rep.':
            return 'kp'
        elif country_name == 'Korea, Rep.':
            return 'kr'
        elif country_name == 'Iran, Islamic Rep.':
            return 'ir'
        elif country_name == 'Egypt, Arab Rep.':
            return 'eg'
        elif country_name == ' Congo, Dem. Rep.':
            return 'cd'
        elif country_name == 'Congo, Rep.':
            return 'cg'
    # if country not found, return none
    return None

