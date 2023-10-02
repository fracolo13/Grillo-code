from obspy import read, Trace, Stream
from obspy.geodetics import kilometer2degrees, locations2degrees
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as pld
from obspy import UTCDateTime
import matplotlib.dates as mdates

csv_path = 'stations_np.csv'


station_coords = {}
epi_lat = 26.9086
epi_lon = 86.3174
st = read('arch_230506T075627_230506T081627_qmnn.mseed')
st.detrend('linear')
st = st.select(channel = 'BNY')
st.trim(starttime = UTCDateTime(2023,5,6,8,1,10), endtime = UTCDateTime(2023,5,6,8,3,7))
distances = []
with open(csv_path, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        station_name = row['Station']
        lat = float(row['Latitude'])
        lon = float(row['Longitude'])
        dist = locations2degrees(epi_lat, epi_lon, lat, lon)
        station_coords[station_name] = {'latitude': lat, 'longitude': lon, "distance": dist}


from obspy import read


for tr in st:
    station_name = tr.stats.station
    if station_name in station_coords:
        distance = station_coords[station_name]['distance']
        pos = tr.data/150 + (distance *111.3)

        plt.plot(tr.times("matplotlib"), pos, lw = 0.5, color = [0,0,0])

xfmt = mdates.DateFormatter('%H:%M:%S')
plt.gca().xaxis.set_major_formatter(xfmt)
plt.show()
        





