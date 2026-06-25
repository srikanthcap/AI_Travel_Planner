import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_itinerary(
    source,
    destination,
    duration,
    budget,
    interests
):

    prompt = f"""
Create a complete travel itinerary.

Source: {source}
Destination: {destination}
Duration: {duration} days
Budget: ₹{budget}
Interests: {interests}

Include:

1. Day-wise itinerary

2. Top attractions

3. Recommended hotels
   - 3 Budget Hotels
   - 3 Mid-range Hotels
   - 3 Luxury Hotels
   Mention approximate price per night.

4. Local cuisine

5. Local beverages

6. Transportation options

7. Estimated total cost

8. Travel tips
"""

    response = model.generate_content(prompt)

    return response.text


def generate_hotel_recommendations(
    destination,
    budget
):

    prompt = f"""
Recommend hotels in {destination}.

Budget: ₹{budget}

Provide:

1. Budget Hotels (3)
2. Mid-range Hotels (3)
3. Luxury Hotels (3)

For each hotel mention:
- Hotel Name
- Approximate Price Per Night
- Rating (Approximate)
- Short Description
"""

    response = model.generate_content(prompt)

    return response.text