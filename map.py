# coding: utf-8
import os
import re
import sys

# Indexes are Python already (0-start)
STATION_ID_POS = 0
LST_DATE_POS = 3
LST_TIME_POS = 4
LONGITUDE_POS = 6
LATITUDE_POS = 7
AVG_TEMP_POS = 9
MAX_TEMP_POS = 10
MIN_TEMP_POS = 11

THRESHOLD = 15
MAX_THRESHOLD = 30

def getLines(line):
    data = line.split()
    if not data[MAX_TEMP_POS].startswith('-99') and not data[MIN_TEMP_POS].startswith('-99') and \
            (float(data[MAX_TEMP_POS]) >= float(data[MIN_TEMP_POS])) and (float(data[MAX_TEMP_POS]) < 60.0):
        
        # Considering the numbers where one of the values is 0 and diff is higher than the threshold
        if (((float(data[MAX_TEMP_POS]) == 0) or float(data[MIN_TEMP_POS]) == 0) and \
        	abs(abs(float(data[MAX_TEMP_POS])) - abs(float(data[MIN_TEMP_POS]))) > THRESHOLD):
        	return

        # Considering values where diff is bigger than another threshold
        if abs(abs(float(data[MAX_TEMP_POS])) - abs(float(data[MIN_TEMP_POS]))) > MAX_THRESHOLD:
        	return

        # If there's a -9999.0 in any column (up to 27, all the others to the right are -9999.0) also ignore
        if '-9999.0' in data[0:27]:
        	return

        print(data[STATION_ID_POS] + "," + data[LATITUDE_POS] + " " + data[LONGITUDE_POS] + " " + data[LST_DATE_POS] +
              " " + data[LST_TIME_POS] + " " + str(abs(abs(float(data[MAX_TEMP_POS])) - abs(float(data[MIN_TEMP_POS])))))


# Parse entries
if __name__ == '__main__':
    for filename in sys.stdin:
        getLines(filename.replace('\n', ''))
