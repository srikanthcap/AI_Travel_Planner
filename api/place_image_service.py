import requests
import os
from dotenv import load_dotenv

load_dotenv()

UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")


def get_place_image(place_name):

    url = "https://api.unsplash.com/search/photos"

    params = {
        "query": place_name,
        "per_page": 1,
        "client_id": UNSPLASH_ACCESS_KEY
    }

    try:

        response = requests.get(url, params=params)

        if response.status_code == 200:

            data = response.json()

            if len(data["results"]) > 0:

                return data["results"][0]["urls"]["regular"]

    except:
        pass

    return "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"