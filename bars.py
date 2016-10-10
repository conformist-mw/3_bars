import json
from math import sin, cos, sqrt, atan2, radians
import argparse


def load_data(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data


def get_biggest_bar(data):
    """ return the biggest bar"""
    seats = {}
    for bar in data:
        seats[bar['Cells']['Name']] = bar['Cells']['SeatsCount']
    return max(seats, key=seats.get)


def get_smallest_bar(data):
    """ return the smallest bar"""
    seats = {}
    for bar in data:
        if bar['Cells']['SeatsCount'] > 0:
            seats[bar['Cells']['Name']] = bar['Cells']['SeatsCount']
    return min(seats, key=seats.get)


def get_closest_bar(data, longitude, latitude, R=6373.0):
    """ return closest bar"""
    dists = {}
    for bar in data:
        lat, lon = bar['Cells']['geoData']['coordinates']
        dlon = radians(lon - longitude)
        dlat = radians(lat - latitude)
        a = sin(dlat / 2) ** 2 + cos(latitude) * cos(lat) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        dists[bar['Cells']['Name']] = R * c
    return min(dists, key=dists.get)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Рассчитывает данные о барах из файла json')
    parser.add_argument('filepath', help='укажите файл в формате json')
    args = parser.parse_args()
    data = load_data(args.filepath)
    print('Самый большой бар: {}'.format(get_biggest_bar(data)))
    print('Самый маленький бар: {}'.format(get_smallest_bar(data)))
    print('Введите ваши координаты: ')
    u_lon = float(input('Долгота: '))
    u_lat = float(input('Широта: '))
    print('Самый близкий бар: {}'.format(get_closest_bar(data, u_lon, u_lat)))
