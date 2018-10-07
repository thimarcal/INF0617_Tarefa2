# coding: utf-8

import sys

DIFF = 'difference'
TIME = 'time'
DATE = 'date'
LAT = 'latitude'
LONG = 'longitude'

def format_date(dateStr):
    return dateStr[0:4]+"-"+dateStr[4:6]+"-"+dateStr[6:]

stations = {}
for line in sys.stdin:
    station, data = line.split(",")
    longitude, latitude, date, time, difference = data.split()

    try:
        if float(stations[station][DIFF]) < float(difference):
            print(longitude, latitude, date, time, difference)
            stations[station][DATE] = date
            stations[station][TIME] = time
        stations[station][DIFF] = max(float(stations[station][DIFF]), float(difference))
    except:
        stations[station] = {}
        print("Adding for "+station, difference)
        stations[station][DIFF] = difference
        stations[station][LAT] = latitude
        stations[station][LONG] = longitude
        stations[station][DATE] = date
        stations[station][TIME] = time

max_diff = {}
max = 0.0
for station in stations.keys():
    if float(stations[station][DIFF]) > max:
        max = float(stations[station][DIFF])
        max_diff = stations[station]

print("Station at (" + str(max_diff[LAT]) + ", " + str(max_diff[LONG]) + ") measured " + str(max_diff[DIFF])
      + " degree(s) difference at " + format_date(str(max_diff[DATE])) + " " + str(max_diff[TIME]))
