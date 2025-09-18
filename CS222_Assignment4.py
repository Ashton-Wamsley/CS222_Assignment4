import json
import ssl
from urllib.request import urlopen

def getForecastUrl():
    pointUrl = "https://api.weather.gov/points/40.1934,-85.3864"
    context = ssl._create_unverified_context()
    response = urlopen(pointUrl, context = context)
    pointData = json.loads(response.read())
    return pointData["properties"] ["forecast"]
    
def getForecastPeriods(forecastUrl):
    context = ssl._create_unverified_context()
    response = urlopen(forecastUrl, context = context)
    forecastData = json.loads(response.read())
    return forecastData["properties"] ["periods"]

def printForecast(period):
    return f"{period["name"]}: {period["temperature"]} Fahrenheit\nDetails: {period["detailedForecast"]}\n"

def main(): 
    forecastUrl = getForecastUrl()
    periods = getForecastPeriods(forecastUrl)
    for period in periods[:14]: 
        print(printForecast(period))

main()