import json
from math import sqrt


def load_data(filepath):
    with open(filepath, 'r', encoding="cp1251") as data_file:
        data = json.loads(data_file.read())
    return data


def get_biggest_bar(data):
    biggets_bar = max(data, key=lambda x : x['SeatsCount'])
    return biggets_bar['Address']


def get_smallest_bar(data):
    smallest_bar = min(data, key=lambda x : x['SeatsCount'])
    return smallest_bar['Address']


def get_closest_bar(data, longitude, latitude):
    closest_bar = min(data, key=lambda x: sqrt(pow(float(x['Longitude_WGS84'])\
        - longitude, 2) + pow(float(x['Latitude_WGS84']) - latitude, 2)))
    return closest_bar['Address']

if __name__ == '__main__':
    filepath = input('Path to file >> ')
    data = load_data(filepath)
    print('Biggest bar:', get_biggest_bar(data))
    print('Smallest bar:', get_smallest_bar(data))
    latitude = float(input('Input latitude >> '))
    longitude = float(input('Input longitude >> '))
    print('Closest bar:', get_closest_bar(data, longitude, latitude))
