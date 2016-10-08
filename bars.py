import json
from math import sin, cos, sqrt, atan2, radians


def load_data(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data


def get_biggest_bar(data):
    seats = {}
    for bar in data:
        seats[bar['Cells']['Name']] = bar['Cells']['SeatsCount']
    return [k for k, v in seats.items() if v == max(seats.values())]


def get_smallest_bar(data):
    seats = {}
    for bar in data:
        if bar['Cells']['SeatsCount'] > 0:
            seats[bar['Cells']['Name']] = bar['Cells']['SeatsCount']
    return [k for k, v in seats.items() if v == min(seats.values())]


def get_closest_bar(data, longitude, latitude, R=6373.0):
    dists = {}
    for bar in data:
        lat, lon = bar['Cells']['geoData']['coordinates']
        dlon = radians(lon - longitude)
        dlat = radians(lat - latitude)
        a = sin(dlat / 2) ** 2 + cos(latitude) * cos(lat) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        dists[bar['Cells']['Name']] = round(R * c, 3)
    return [k for k, v in dists.items() if v == min(dists.values())]


if __name__ == '__main__':
    pass
