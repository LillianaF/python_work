import csv
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/world_fires_7_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    '''for index, column_header in enumerate(header_row):
        print(index, column_header)'''

    # Get dates, lons, lats, and brightness
    dates, lons, lats, brightness = [], [], [], []
    # count = 0
    for row in reader:
        # count = count + 1
        # print(count)
        date = datetime.strptime(row[5], '%Y-%m-%d')
        bright = float(row[2])
        dates.append(date)
        lons.append(row[1])
        lats.append(row[0])
        brightness.append(bright)

# Map the fires
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [bright/20 for bright in brightness],
    },
}]
my_layout = Layout(title='Global Fires', title_x=0.5)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')

# print(lats[:5])
