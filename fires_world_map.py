import csv
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

num_rows = 15_000

filename = 'data/world_fires_7_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    '''for index, column_header in enumerate(header_row):
        print(index, column_header)'''

    # Get dates, lons, lats, and brightness
    lons, lats, brightness, dates, hover_texts = [], [], [], [], []
    # count = 0
    row_num = 0
    for row in reader:
        # count = count + 1
        # print(count)
        # int(float(row[1]))
        bright = float(row[2])
        date = datetime.strptime(row[5], '%Y-%m-%d')
        label = f"{date.strftime('%m/%d/%y')} - {bright}"
        lons.append(row[1])
        lats.append(row[0])
        brightness.append(bright)
        dates.append(date)
        hover_texts.append(label)

        row_num += 1
        if row_num == num_rows:
            break

# Map the fires
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [bright/20 for bright in brightness],
        'color': brightness,
        'colorscale': 'Oranges',
        'reversescale': False,
        'colorbar': {'title': 'Brightness'},
    },
}]
my_layout = Layout(title='Global Fires', title_x=0.5)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')
# print(brightness[:5])
