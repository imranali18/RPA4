import urllib.request
import json

url = "http://nominatim.openstreetmap.org/"\
      "search?q={}&format=json&polygon_geojson=1&addressdetails=0"\
      .format('Troy,NY')
f = urllib.request.urlopen(url)
rawcontent = f.read()
content = json.loads(rawcontent.decode("utf-8"))
