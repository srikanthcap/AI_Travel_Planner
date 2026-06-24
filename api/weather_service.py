import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={API_KEY}"
        f"&units=metric"
    )

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return None