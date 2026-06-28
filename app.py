import streamlit as st
import json

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
from api.attractions_service import get_famous_places
from api.place_image_service import get_place_image


st.set_page_config(
    page_title="AI Travel Planner",
    layout="wide"
)

# ---------- CUSTOM UI ----------
st.markdown("""
<style>

.stApp{
    background: #0f172a;
}

/* Hero */
.hero-title{
    font-size:58px;
    font-weight:800;
    color:white;
    margin-bottom:10px;
}

.hero-subtitle{
    font-size:28px;
    font-weight:700;
    color:white;
    margin-bottom:10px;
}

.hero-text{
    color:#cbd5e1;
    font-size:18px;
    margin-bottom:30px;
}

/* Cards */
.card-box{
    background:#1e293b;
    border:1px solid #334155;
    border-radius:18px;
    padding:25px;
    min-height:180px;
    margin-bottom:20px;
}

.card-box h3{
    margin-bottom:15px;
}

.card-box h1{
    font-size:48px;
    margin-bottom:10px;
}

.card-box p{
    color:#cbd5e1;st.metric("Travel Cost", f"₹{travel_cost}")
st.metric("Hotel Cost", f"₹{hotel_cost}")
}

/* Inputs */
.stTextInput input,
.stNumberInput input{
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
create_table()

# ---------- PROFESSIONAL HERO SECTION ----------

st.markdown("""

<style>

.hero-box{
    background-image:url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e");
    background-size:cover;
    background-position:center;
    padding:60px;
    border-radius:25px;
    margin-bottom:25px;
}

.hero-heading{
    color:white;
    font-size:55px;
    font-weight:800;
}

.hero-sub{
    color:white;
    font-size:24px;
}

.card-box{
    background:#1e293b;
    border:1px solid #334155;
    border-radius:18px;
    padding:20px;
    text-align:center;
    height:160px;
}

.card-box h3{
    color:white;
}

.card-box h2{
    color:#38bdf8;
}

</style>

""", unsafe_allow_html=True)

st.markdown("""

<div class="hero-box">
    <div class="hero-heading">🌍 AI Powered Travel Planner</div>
    <div class="hero-sub">✈️ Plan Smarter, Travel Better</div>
</div>
""", unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown('<div class="card-box"><h3>🌍 Destinations</h3><h2>100+</h2></div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card-box"><h3>🤖 AI Powered</h3><h2>Gemini</h2></div>', unsafe_allow_html=True)

with c3:
    st.markdown('<div class="card-box"><h3>📄 PDF Reports</h3><h2>Available</h2></div>', unsafe_allow_html=True)

with c4:
    st.markdown('<div class="card-box"><h3>☁️ Live Weather</h3><h2>Enabled</h2></div>', unsafe_allow_html=True)

st.markdown("## 🧳 Plan Your Trip")

left,right = st.columns(2)

with left:
    source = st.text_input("📍 Source Location")
    destination = st.text_input("🏖 Destination")
    start_date = st.date_input("📅 Start Date")

with right:
    duration = st.number_input(
    "⏳ Duration (Days)",
    min_value=1,
    max_value=30
    )


budget = st.number_input(
    "💰 Budget (₹)",
    min_value=1000
)

interests = st.multiselect(
    "🎯 Interests",
    [
        "Adventure",
        "Food",
        "History",
        "Nature",
        "Shopping",
        "Photography"
    ]
)


c1,c2,c3 = st.columns([1,2,1])

with c2:
    generate_btn = st.button(
    "🚀 Generate Travel Plan",
    use_container_width=True
    )

# Generate Plan

if generate_btn:

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

    travel_cost = min(2000, int(budget * 0.30))
    hotel_cost = min(duration * 2500, int(budget * 0.50))

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
    f"₹{budget_data['travel_cost']}"
    )

    col2.metric(
        "Hotel Cost",
        f"₹{budget_data['hotel_cost']}"
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
        st.subheader("📍 Famous Attractions")

        attractions = get_famous_places(destination)

        if attractions:

            for place in attractions:

                image = get_place_image(
                    f"{place['name']} {destination}"
                )

                col1, col2 = st.columns([1, 2])

                with col1:

                    st.image(
                        image,
                        use_container_width=True
                    )

                with col2:

                    st.markdown(f"## 📍 {place['name']}")

                    st.write(place["description"])

                    st.success(
                        f"🌤 Best Time : {place['best_time']}"
                    )

                    st.info(
                        f"🎫 Entry Fee : {place['entry_fee']}"
                    )

                    st.warning(
                        f"⭐ Rating : {place['rating']}"
                    )

                    st.link_button(
                        "📍 Open in Google Maps",
                        f"https://www.google.com/maps/search/{place['name']} {destination}"
                    )

                st.divider()

        else:

                st.warning("No attractions found.")
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
        # Analytics Dashboard

        st.subheader("📊 Travel Analytics")

        if not history.empty:

            st.metric(
                "Total Trips Generated",
                len(history)
            )

            st.subheader(
                "💰 Budget Analysis Chart"
            )

            st.bar_chart(
                history["budget"]
            )

            st.subheader(
                "🌍 Most Visited Destinations"
            )

            st.bar_chart(
                history["destination"].value_counts()
            )