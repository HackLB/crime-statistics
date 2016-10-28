#!/usr/bin/env python
import os, sys
import requests
import simplejson as json

from xmljson import Parker
from xml.etree.ElementTree import fromstring

url ='http://api.ezaxess.com/v2/pd/longbeach/crimes/all'


def get_crime_data():
    """
    Fetches XML data, converts to JSON using Parker syntax
    """
    print('Getting crime data...')
    r = requests.get(url)
    bf = Parker(dict_type=dict)
    obj = bf.data(fromstring(r.text))
    return obj


def cleanup_crime_data(records):
    """
    Unwraps outer dict (item), and then cleans up a few values
    """
    print('Cleaning crime data...')
    cleaned_data = []
    for record in records['item']:
        record['description'] = record['description'].strip()
        record['title'] = record['title'].strip()
        cleaned_data.append(record)
    return cleaned_data


def get_subdirectory(base_name):
    """
    Takes the base filename and returns a path to a subdirectory, creating it if needed.
    For example, given the base name 0003168449, returns a path like:
    ./_data/0003/16/84
    """
    sub_dir = os.path.join(data_path, base_name[0:-6], base_name[-6:-4], base_name[-4:-2])
    os.makedirs(sub_dir, exist_ok=True)
    return sub_dir


def save_crime_data(records):
    """
    Receives cleaned up data as Python list of dicts, and saves each
    item in the list as a JSON object. Uses a get_subdirectory function
    to allow for splitting up files into subdirectories as needed.
    """
    print('Saving crime data...')
    for record in records:
        base_name = str(record['id']).zfill(10)
        file_name = '{}.json'.format(base_name)

        directory = get_subdirectory(base_name)
        path = os.path.join(directory, file_name)

        with open(path, 'w') as f:
            json.dump(record, f, indent=4, ensure_ascii=False, sort_keys=True)


if __name__ == "__main__":
    repo_path = os.path.dirname(os.path.realpath(sys.argv[0])) # Path to current directory
    data_path = os.path.join(repo_path, '_data')               # Root path for record data
    os.makedirs(data_path, exist_ok=True)                      # Create _data directory

    data = get_crime_data()                                    # Fetch crime data as JSON
    cleaned_data = cleanup_crime_data(data)                    # A little bit of cleanup
    save_crime_data(cleaned_data)                              # Save it into _data

