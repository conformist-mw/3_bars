import json
from math import sin, cos, sqrt, atan2, radians


def load_data(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data


def get_biggest_bar(data):
    seats = []
    for bar in data:
        seats.append(bar['Cells']['SeatsCount'])
    seat = sorted(seats)[-1]
    bar_name = []
    for bar in data:
        if bar['Cells']['SeatsCount'] == seat:
            bar_name.append(bar['Cells']['Name'])
    return bar_name


def get_smallest_bar(data):
    seats = []
    for bar in data:
        seats.append(bar['Cells']['SeatsCount'])
    seat = sorted([x for x in seats if x > 0])[0]
    bar_name = []
    for bar in data:
        if bar['Cells']['SeatsCount'] == seat:
            bar_name.append(bar['Cells']['Name'])
    return bar_name


def get_closest_bar(data, longitude, latitude, R=6373.0):
    ''' fix me:
        if round(distance, 2) there might be several
        min values. Can be returned a list of places'''
    d = {}
    for bar in data:
        lat, lon = bar['Cells']['geoData']['coordinates']
        dlon = radians(lon - longitude)
        dlat = radians(lat - latitude)
        a = sin(dlat / 2) ** 2 + cos(latitude) * cos(lat) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        d[bar['Cells']['Name']] = R * c
    return min(d, key=d.get)


if __name__ == '__main__':
    pass