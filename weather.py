import requests

def get_weather(city):
    url=f"https://wttr.in/{city}?format=j1"
    r=requests.get(url)
    return r.json()