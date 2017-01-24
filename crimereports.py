#!/usr/bin/env python
import os, sys
import requests
import simplejson as json
from pprint import pprint


url ='https://www.crimereports.com/api/crimes/details.json?agency_id=83&days=sunday,monday,tuesday,wednesday,thursday,friday,saturday&end_date=2017-01-23&end_time=23&incident_types=Assault,Assault+with+Deadly+Weapon,Breaking+%26+Entering,Disorder,Drugs,Homicide,Kidnapping,Liquor,Other+Sexual+Offense,Property+Crime,Property+Crime+Commercial,Property+Crime+Residential,Quality+of+Life,Robbery,Sexual+Assault,Sexual+Offense,Theft,Theft+from+Vehicle,Theft+of+Vehicle&include_sex_offenders=false&lat1=33.84860560385033&lat2=33.78542513929222&lng1=-118.02457809448242&lng2=-118.25426101684569&sandbox=false&start_date=2017-01-09&start_time=0&zoom=13'


def get_crime_data():
    """
    Fetches XML data, converts to JSON using Parker syntax
    """
    print('Getting crime data...')
    try:
        r = requests.get(url)
        return r.json()['agencies'][0]['crimes']
    except:
        return None


def cleanup_crime_data(records):
    """
    Unwraps outer dict (item), and then cleans up a few values
    """
    print('Cleaning crime data...')
    return records


def get_subdirectory(base_name):
    """
    Takes the base filename and returns a path to a subdirectory, creating it if needed.
    For example, given the base name 0003168449, returns a path like:
    ./_data/0003/16/84
    """
    # sub_dir = os.path.join(data_path, base_name[0:-6], base_name[-6:-4], base_name[-4:-2])
    # os.makedirs(sub_dir, exist_ok=True)
    # return sub_dir
    return data_path


def save_crime_data(records):
    """
    Receives cleaned up data as Python list of dicts, and saves each
    item in the list as a JSON object. Uses a get_subdirectory function
    to allow for splitting up files into subdirectories as needed.
    """
    print('Saving crime data...')
    for record in records:
        base_name = record['primary_key']
        file_name = '{}.json'.format(base_name)

        directory = get_subdirectory(base_name)
        path = os.path.join(directory, file_name)

        with open(path, 'w') as f:
            json.dump(record, f, indent=4, ensure_ascii=False, sort_keys=True)


if __name__ == "__main__":
    repo_path = os.path.dirname(os.path.realpath(sys.argv[0])) # Path to current directory
    data_path = os.path.join(repo_path, '_crdata')               # Root path for record data
    os.makedirs(data_path, exist_ok=True)                      # Create _data directory

    data = get_crime_data()                                    # Fetch crime data as JSON
    pprint(data)
    cleaned_data = cleanup_crime_data(data)                    # A little bit of cleanup
    save_crime_data(cleaned_data)                              # Save it into _data

