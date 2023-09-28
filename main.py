import urllib.parse, urllib.request, urllib.error
import json
from pprint import pprint
import ssl
from googletrans import Translator


def en_to_uk(text):
    translator = Translator()
    return translator.translate(text, src="en", dest="uk").text

def kelvin_to_celsius(t):
    return t - 273.15


def get_city_weather_data(city: str, data=None):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    weather_API_key = "f5cb1021b65e71408c077f3aff50c678"
    host_link = "https://api.openweathermap.org/data/2.5/weather?"
    arguments = {}
    arguments["q"] = city
    arguments["appid"] = weather_API_key
    args_link = urllib.parse.urlencode(arguments)
    full_link = host_link + args_link

    while data is None:
        try:
            with urllib.request.urlopen(full_link, context=ctx) as uh:
                data = uh.read().decode()
                js_dct = json.loads(data)
                return js_dct
        except urllib.error.HTTPError:
            print("wrong city name")


city = input("Введіть місто:\n")
city_json_data = get_city_weather_data(city)
if city_json_data:
    pprint(city_json_data)
    print(f"Місто {city}:\n"
          f"Температура: {kelvin_to_celsius(city_json_data['main']['temp'])}\n"
          f"Погода: {en_to_uk(city_json_data['weather'][0]['description'])}")
