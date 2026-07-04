import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"

    response = requests.get(
        url,
        timeout=20
    )

    response.raise_for_status()

    data = response.json()

    if "current_condition" not in data:
        raise ValueError(
            "Current weather data missing"
        )

    return data