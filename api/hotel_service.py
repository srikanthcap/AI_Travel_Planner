import google.generativeai as genai
import os
import json

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")


def get_hotels(destination):

    prompt = f"""
Return ONLY JSON.

Suggest 5 best hotels in {destination}.

Format:

[
 {{
   "name":"",
   "rating":"",
   "price":"",
   "description":""
 }}
]

No markdown.
Only JSON.
"""

    response = model.generate_content(prompt)

    text = response.text.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(text)
    except:
        return []