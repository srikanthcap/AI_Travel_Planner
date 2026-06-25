from api.gemini_service import model


def get_travel_options(source, destination):

    prompt = f"""
    Suggest travel options from {source} to {destination}.

    Include:

    1. Flight
    2. Train
    3. Bus
    4. Car

    Mention:
    - Estimated Cost
    - Estimated Travel Time

    Finally recommend the best option.

    Format neatly.
    """

    response = model.generate_content(prompt)

    return response.text