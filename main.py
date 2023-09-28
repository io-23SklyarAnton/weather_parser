import urllib.parse, urllib.request, urllib.error
import json
from pprint import pprint

weather_API_key = "f5cb1021b65e71408c077f3aff50c678"
host_link = "https://api.openweathermap.org/data/2.5/weather?"
arguments = {}
city = input("Enter your city:\n")
arguments["q"] = city
arguments["appid"] = weather_API_key
args_link = urllib.parse.urlencode(arguments)
full_link = host_link + args_link
with urllib.request.urlopen(full_link) as uh:
    print(uh.headers)
    data = uh.read().decode()
    js_dct = json.loads(data)
    pprint(data)

