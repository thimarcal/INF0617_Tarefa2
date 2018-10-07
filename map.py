# coding: utf-8
import os
import re
import sys

# Indexes are Python already (0-start)
STATION_ID_POS = 0
UTC_DATE_POS = 1
UTC_TIME_POS = 2
LONGITUDE_POS = 6
LATITUDE_POS = 7
AVG_TEMP_POS = 9
MAX_TEMP_POS = 10
MIN_TEMP_POS = 11

#os.chdir('D:\\Thiago\\Studies\\Unicamp\\MDC\\INF-617\\Tarefas\\INF0617_Tarefa2')
os.chdir('/mnt/d/Thiago/Studies/Unicamp/MDC/INF-617/Tarefas/INF0617_Tarefa2')

def getLines(filename):
    file = open('./weather-2017/' + filename, encoding='utf-8', errors='ignore')
    for line in file:
        data = line.split()
        if not data[MAX_TEMP_POS].startswith('-99') and not data[MIN_TEMP_POS].startswith('-99') and \
                (float(data[MAX_TEMP_POS]) >= float(data[MIN_TEMP_POS])) and (float(data[MAX_TEMP_POS]) < 60.0):
            print(data[STATION_ID_POS] + "," + data[LATITUDE_POS] + " " + data[LONGITUDE_POS] + " " + data[UTC_DATE_POS] +
                  " " + data[UTC_TIME_POS] + " " + str(abs(abs(float(data[MAX_TEMP_POS])) - abs(float(data[MIN_TEMP_POS])))))


# Parse entries
if __name__ == '__main__':
    for filename in sys.stdin:
        getLines(filename.replace('\n', ''))
