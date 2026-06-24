import streamlit as st
from api.gemini_service import generate_itinerary
from api.weather_service import get_weather

st.set_page_config(
    page_title="AI Travel Planner",
    layout="wide"
)

st.title("🌍 AI Powered Travel Planner")

source = st.text_input("Source Location")

destination = st.text_input("Destination")

start_date = st.date_input("Start Date")

duration = st.number_input(
    "Duration (Days)",
    min_value=1,
    max_value=30
)

budget = st.number_input(
    "Budget (₹)",
    min_value=1000
)

interests = st.multiselect(
    "Interests",
    [
        "Adventure",
        "Food",
        "History",
        "Nature",
        "Shopping",
        "Photography"
    ]
)

weather = get_weather(destination)

if weather:

    st.subheader("🌤 Current Weather")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Temperature",
        f"{weather['main']['temp']} °C"
    )

    col2.metric(
        "Humidity",
        f"{weather['main']['humidity']}%"
    )

    col3.metric(
        "Wind Speed",
        f"{weather['wind']['speed']} m/s"
    )

    col4.metric(
        "Condition",
        weather['weather'][0]['main']
    )

if st.button("Generate Travel Plan"):

    with st.spinner("Generating itinerary..."):

        itinerary = generate_itinerary(
            source,
            destination,
            duration,
            budget,
            interests
        )

        st.subheader("Generated Itinerary")

        st.write(itinerary)