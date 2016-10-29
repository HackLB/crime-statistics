#!/usr/bin/env python
import os, sys
import requests
import simplejson as json
from pprint import pprint


def cleanup_legacy_data(records):
    """
    Unwraps outer dict (item), and then cleans up a few values
    """
    print('Cleaning crime data...')
    cleaned_data = []
    for record in records['results']:
        cleaned = {}

        cleaned['block_address'] = record['block'].strip()
        cleaned['case_number'] = int(record['caseID'])
        cleaned['city'] = 'Long Beach'
        cleaned['state'] = 'CA'

        cleaned['date_occured'] = record['occurred']['iso'].replace('T', ' ').replace('.000Z', ' UTC')

        cleaned['incident_id'] = int(record['incident'])

        cleaned['description'] = record['description'].strip()
        if len(cleaned['description']) == 0:
            cleaned['description'] = None

        cleaned['title'] = record['title'].strip()
        cleaned['latitude'] = record['location']['latitude']
        cleaned['longitude'] = record['location']['longitude']

        pprint(cleaned)
        cleaned_data.append(cleaned)
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


def save_legacy_data(records):
    """
    Receives cleaned up data as Python list of dicts, and saves each
    item in the list as a JSON object. Uses a get_subdirectory function
    to allow for splitting up files into subdirectories as needed.
    """
    print('Saving crime data...')
    for record in records:
        base_name = str(record['case_number']).zfill(12)
        file_name = '{}.json'.format(base_name)

        directory = get_subdirectory(base_name)
        path = os.path.join(directory, file_name)

        with open(path, 'w') as f:
            json.dump(record, f, indent=4, ensure_ascii=False, sort_keys=True)


if __name__ == "__main__":
    repo_path = os.path.dirname(os.path.realpath(sys.argv[0])) # Path to current directory
    data_path = os.path.join(repo_path, '_data_old')               # Root path for record data
    os.makedirs(data_path, exist_ok=True)                      # Create _data directory

    path = '/Users/rogerhoward/Desktop/crime.json'

    with open(path) as json_data:
        data = json.load(json_data)

    cleaned_data = cleanup_legacy_data(data)
    save_legacy_data(cleaned_data)

    # data = get_crime_data()                                    # Fetch crime data as JSON
    # cleaned_data = cleanup_crime_data(data)                    # A little bit of cleanup
    # save_crime_data(cleaned_data)                              # Save it into _data

