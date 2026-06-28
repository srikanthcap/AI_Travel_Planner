import google.generativeai as genai
import os
import json


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def get_famous_places(destination):

    prompt = f"""
You are an expert travel guide.

Destination: {destination}

Return ONLY valid JSON.

IMPORTANT RULES:

1. Return ONLY famous tourist attractions located in {destination}.
2. Do NOT include attractions from any other city, state, or country.
3. Return exactly 5 attractions.
4. Each attraction must actually exist in {destination}.
5. Description should be 2-3 lines.
6. Include realistic best_time, entry_fee, and rating.

Format:

[
  {{
    "name":"",
    "description":"",
    "best_time":"",
    "entry_fee":"",
    "rating":""
  }}
]

Only JSON.
No markdown.
No explanation.
"""


    try:

        response = model.generate_content(prompt)

        text = response.text.replace(
            "```json",
            ""
        ).replace(
            "```",
            ""
        ).strip()

        print("========== GEMINI RESPONSE ==========")
        print(text)

        return json.loads(text)

    except Exception as e:

        print("Gemini Error:", e)

        return []