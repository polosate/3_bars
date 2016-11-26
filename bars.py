import json
from math import sqrt


def load_data(filepath):
    with open(filepath, 'r', encoding="cp1251") as data_file:
        data = json.loads(data_file.read())
    return data


def sort_by_seats_count(item):
    return item['SeatsCount']


def bar_names(data):
    seat_count = data[0]['SeatsCount']
    result = []
    for item in data:
        if item['SeatsCount'] == seat_count:
            result.append(item['Name'])
    return result


def get_biggest_bar(data):
    data.sort(key=sort_by_seats_count, reverse=True)
    return bar_names(data)


def get_smallest_bar(data):
    data.sort(key=sort_by_seats_count)
    return bar_names(data)


def get_closest_bar(data, longitude, latitude):
    data.sort(key=lambda item: sqrt(pow(float(item['Longitude_WGS84']) - longitude, 2) \
        + pow(float(item['Latitude_WGS84']) - latitude, 2)))
    return data[0]['Name']


if __name__ == '__main__':
    data = load_data('data-2897-2016-11-23.json')
    print(get_biggest_bar(data))
    print(get_smallest_bar(data))
    latitude = float(input('Input latitude >> '))
    longitude = float(input('Input longitude >> '))
    print(get_closest_bar(data, longitude, latitude))
