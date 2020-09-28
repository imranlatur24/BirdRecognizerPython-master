import json
import urllib.request

geourl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson"
response = urllib.request.urlopen(geourl)
content = response.read()
data = json.loads(content.decode('utf8'))
print(data)
#print(data(type))

