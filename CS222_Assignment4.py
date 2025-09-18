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

import unittest

class TestForectCast(unittest.TestCase):
    def testPrintForecast(self):
        sample = {
            "name" : "Tonight", "temperature" : 65, "detailedForecast": "Clear skies with light winds."
        }
        expected = "Tonight: 65 Fahrenheit\nDetails: Clear skies with light winds.\n"
        self.assertEqual(printForecast(sample), expected)
    
    def testGetForecastUrl(self):
        testUrl = getForecastUrl()
        self.assertTrue(testUrl.startswith("https://api.weather.gov/gridpoints/"))
    
if __name__ == "__main__":
    unittest.main()
