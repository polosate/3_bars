import json
from math import sqrt


def load_data(filepath):
    with open(filepath, 'r', encoding="utf-8") as data_file:
        all_bars = json.loads(data_file.read())
    return all_bars


def get_address_of_biggest_bar(all_bars):
    biggets_bar = max(all_bars, key=lambda x : x['SeatsCount'])
    return biggets_bar['Address']


def get_address_of_smallest_bar(all_bars):
    smallest_bar = min(all_bars, key=lambda x : x['SeatsCount'])
    return smallest_bar['Address']


def get_address_of_closest_bar(all_bars, longitude, latitude):
    closest_bar = min(all_bars, key=lambda x: sqrt(pow(float(x['Longitude_WGS84'])\
        - longitude, 2) + pow(float(x['Latitude_WGS84']) - latitude, 2)))
    return closest_bar['Address']

if __name__ == '__main__':
    filepath = input('Path to file >> ')
    all_bars = load_data(filepath)
    print('Address of biggest bar:', get_address_of_biggest_bar(all_bars))
    print('Address of smallest bar:', get_address_of_smallest_bar(all_bars))
    latitude = float(input('Input latitude >> '))
    longitude = float(input('Input longitude >> '))
    print('Address of closest bar:', get_address_of_closest_bar(all_bars, longitude, latitude))
