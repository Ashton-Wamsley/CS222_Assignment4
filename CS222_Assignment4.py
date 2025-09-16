import json
import ssl
from urllib.request import urlopen

def main():
    pointUrl = "https://api.weather.gov/points/40.1934,-85.3864"
    context = ssl._create_unverified_context()
    response = urlopen(pointUrl, context = context)
    pointData = json.loads(response.read())
    forecastUrl = pointData["properties"], ["forecast"]
    response = urlopen(forecastUrl, context = context)
    forecastData = json.loads(response.read())
    periods = forecastData["properties"], ["periods"]

    for period in periods[:14]: 
        print(period["name"] + ": " + period["temperature"] + " Farenheit")
        print("Details: " + period["detailedForecast"] + "\n")

main()