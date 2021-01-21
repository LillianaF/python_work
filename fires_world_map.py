import csv
from datetime import datetime

filename = 'data/world_fires_7_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    '''for index, column_header in enumerate(header_row):
        print(index, column_header)'''

    # Get dates, lons, lats, and brightness
    dates, lons, lats, brightness = [], [], [], []
    for row in reader:
        date = datetime.strptime(row[5], '%Y-%m-%d')
        bright = float(row[2])
        dates.append(date)
        lons.append(row[1])
        lats.append(row[0])
        brightness.append(bright)

print(lats[:5])
