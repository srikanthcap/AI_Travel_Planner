import pandas as pd

def get_hotels(city):

    hotels = pd.read_csv("data/hotels.csv")

    hotels["city"] = hotels["city"].astype(str).str.strip().str.lower()

    city = city.strip().lower()

    # Exact match
    result = hotels[
        hotels["city"] == city
    ]

    return result