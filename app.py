import streamlit as st

from api.gemini_service import generate_itinerary
from api.weather_service import get_weather
from api.travel_service import get_travel_options
from api.budget_service import calculate_budget
from database.db import (
    create_table,
    save_trip,
    get_all_trips
)
from api.pdf_service import create_pdf


st.set_page_config(
    page_title="AI Travel Planner",
    layout="wide"
)

st.title("🌍 AI Powered Travel Planner")

create_table()

# User Inputs

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

# Generate Plan

if st.button("Generate Travel Plan"):

    # Weather Section

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

    else:
        st.warning(
            "Weather information not available."
        )

    # Travel Options

    st.subheader("✈️🚆🚌 Travel Options")

    travel = get_travel_options(
        source,
        destination
    )

    st.write(travel)

    # Estimated Costs

    travel_cost = 2000

    hotel_cost = duration * 2500

    # Budget Analysis

    budget_data = calculate_budget(
        budget,
        travel_cost,
        hotel_cost,
        duration
    )

    st.subheader("💰 Budget Analysis")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Travel Cost",
        f"₹{travel_cost}"
    )

    col2.metric(
        "Hotel Cost",
        f"₹{hotel_cost}"
    )

    col3.metric(
        "Food Cost",
        f"₹{budget_data['food_cost']}"
    )

    col4.metric(
        "Remaining Budget",
        f"₹{budget_data['remaining_budget']}"
    )

    st.success(
        f"Estimated Total Cost: ₹{budget_data['total_cost']}"
    )

    # Google Maps Section

    st.subheader("📍 Destination Map")

    maps_url = (
        f"https://www.google.com/maps/search/{destination}"
    )

    st.link_button(
        "📍 Open in Google Maps",
        maps_url
    )

    # AI Itinerary

    with st.spinner("Generating itinerary..."):

        itinerary = generate_itinerary(
            source,
            destination,
            duration,
            budget,
            interests
        )

        save_trip(
            source,
            destination,
            duration,
            budget,
            interests
        )

        st.subheader(
            "🗺 Generated Itinerary"
        )

        st.write(itinerary)

        # PDF Download

        pdf_file = create_pdf(
            itinerary,
            weather
        )

        with open(
            pdf_file,
            "rb"
        ) as file:

            st.download_button(
                label="📄 Download Itinerary PDF",
                data=file,
                file_name="Travel_Itinerary.pdf",
                mime="application/pdf"
            )
        # Trip History

        st.subheader("📜 Trip History")

        history = get_all_trips()

        if not history.empty:

            st.dataframe(
                history,
                use_container_width=True
            )

        else:

            st.info(
                "No trips generated yet."
            )