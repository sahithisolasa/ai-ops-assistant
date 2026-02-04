import requests
import os

def get_weather(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        return {"error": "OPENWEATHER_API_KEY not found"}

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    r = requests.get(url)
    data = r.json()

    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    }
