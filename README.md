# 🌍 SmartTrip AI

### AI-Powered Intelligent Travel Planning Platform

SmartTrip AI is an AI-powered travel planning application that helps users create personalized travel itineraries based on their destination, budget, trip duration, and interests. The application integrates Artificial Intelligence, live weather information, budget estimation, tourist attractions, Google Maps, and PDF itinerary generation into a single platform.

---

## 🚀 Features

- 🤖 AI-generated personalized travel itinerary
- 🌤 Live weather information
- 💰 Smart budget estimation
- ✈ Travel planning assistance
- 📍 Google Maps integration
- 🏛 Famous tourist attractions
- 🖼 Attraction images
- 📄 Download itinerary as PDF
- 📊 Travel analytics dashboard
- 🗃 Trip history storage

---

# 📷 Application Screenshots

## 🏠 Home Page

![Home](screenshots/home.png)

---

## 🌤 Weather & Budget Analysis

![Weather](screenshots/weather_budget.png)

---

## 🗺 AI Generated Itinerary

![Itinerary](screenshots/itinerary.png)

---

## 📍 Famous Attractions

![Attractions](screenshots/attractions.png)

---

## 📊 Analytics Dashboard

![Analytics](screenshots/analytics.png)

---

# 🛠 Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Streamlit | User Interface |
| Google Gemini AI | AI Itinerary Generation |
| OpenWeather API | Live Weather |
| Unsplash API | Attraction Images |
| SQLite | Trip History |
| ReportLab | PDF Generation |

---

# 📂 Project Structure

```text
AI_Travel_Planner/
│
├── api/
│   ├── attractions_service.py
│   ├── budget_service.py
│   ├── gemini_service.py
│   ├── hotel_service.py
│   ├── pdf_service.py
│   ├── place_image_service.py
│   ├── travel_service.py
│   └── weather_service.py
│
├── database/
│
├── screenshots/
│
├── app.py
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/srikanthcap/AI_Travel_Planner.git
```

Go to the project

```bash
cd AI_Travel_Planner
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY

WEATHER_API_KEY=YOUR_OPENWEATHER_API_KEY

UNSPLASH_ACCESS_KEY=YOUR_UNSPLASH_API_KEY
```

---

# 🤖 APIs Used

- Google Gemini API
- OpenWeather API
- Unsplash API
- Google Maps

---

# 📄 PDF Export

Users can download the complete travel itinerary as a professionally formatted PDF report.

---

# 📈 Future Enhancements

- Hotel Booking
- Flight Booking
- Voice Assistant
- User Authentication
- Multi-language Support
- Expense Tracker
- AI Chat Assistant

---

# 👨‍💻 Author

**Srikanth**

GitHub:
https://github.com/srikanthcap

---

# ⭐ If you like this project

Please consider giving this repository a ⭐ on GitHub.