import sys
import requests
from collections import namedtuple

localization = sys.argv[1]

Weather  = namedtuple("Weather", ['location', 'temperature', 'air_pressure', 'humidity'])

# class Weather:
#     def __init__(self, location, temperature):
#         self.location = location
#         self.temperature = temperature


def get_location_id(localization):
    """Pobiera id lokalizacji"""
    resp = requests.get(f"https://www.metaweather.com/api/location/search/?query={localization}")
    location_id = resp.json()[0]['woeid']
    return location_id


# pobietam pogodę dla lokalizacji
def get_loaction_weather(location_id):
    resp = requests.get(f"https://www.metaweather.com/api/location/{location_id}/")
    resp_json = resp.json()['consolidated_weather'][0]

    weather = Weather(
        location = resp.json()['title'],
        temperature= resp_json['the_temp'],
        air_pressure=resp_json['air_pressure'],
        humidity=resp_json['humidity']
    )

    return weather


def print_weather(weather):
    print(f"Pogoda w lokalizacji: {weather.location}")
    print("temperatura: ", weather.temperature)
    print("ciśnienie powietrza: ", weather.air_pressure)
    print("wilgotność: ", weather.humidity)


location_id = get_location_id(localization)
weather = get_loaction_weather(location_id)
print_weather(weather)


input("Wciśnij dowolny klawisz")