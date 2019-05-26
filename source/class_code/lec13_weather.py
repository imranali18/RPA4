import urllib.request
import json

zip_code = input("Enter the ZIP Code => ")
weather_url = 'http://api.openweathermap.org/data/2.5/weather?zip={},us&units=imperial&APPID=bc25f185302a01cfa3d32eb656a309fd'.format(zip_code)
weather_file = urllib.request.urlopen(weather_url)
weather_json = weather_file.read()
print(weather_json)
weather = json.loads(weather_json)
print(weather)
print("Current temperature in {} is {:.2f} F".format(weather["name"], weather["main"]["temp"]))
