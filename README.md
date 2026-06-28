# 🌍 AI Powered Travel Planner

An AI-powered travel planning platform that generates personalized travel itineraries based on destination, budget, duration, and user interests. The application integrates Google Gemini AI, Weather APIs, Budget Analysis, Travel Recommendations, PDF Export, Trip History Tracking, and Analytics Dashboard into a single user-friendly platform.

---

## 📌 Problem Statement

Planning a trip often requires users to search multiple platforms for weather updates, travel options, budget estimation, attractions, and local information.

The objective of this project is to simplify travel planning by providing an intelligent platform that generates personalized travel itineraries while offering weather forecasts, budget analysis, travel insights, and downloadable travel reports.

---

## 🛠️ Tech Stack

| Layer                | Technology        |
| -------------------- | ----------------- |
| Frontend             | Streamlit         |
| AI Engine            | Google Gemini API |
| Programming Language | Python            |
| Database             | SQLite            |
| Weather Service      | OpenWeather API   |
| Data Processing      | Pandas            |
| PDF Generation       | ReportLab         |
| Version Control      | Git & GitHub      |

---

## ✨ Features

### 🤖 AI Itinerary Generation

* Personalized travel plans using Gemini AI
* Day-wise itinerary recommendations
* Tourist attraction suggestions
* Local cuisine recommendations
* Travel tips and guidance

### 🌤 Real-Time Weather Forecast

* Current temperature
* Humidity levels
* Wind speed
* Weather conditions

### ✈️ Travel Recommendations

* Travel suggestions between locations
* Estimated travel expenses
* Transportation guidance

### 💰 Budget Analysis

* Travel cost estimation
* Hotel cost estimation
* Food expense calculation
* Remaining budget analysis

### 🗺️ Google Maps Integration

* Direct destination navigation
* Location visualization
* Easy route access

### 📄 PDF Export

* Download itinerary as PDF
* Travel summary report
* Offline accessibility

### 🗄️ Trip History Management

* Save generated trips
* SQLite database integration
* Historical travel records

### 📊 Analytics Dashboard

* Total trips generated
* Budget analytics
* Destination insights
* Travel statistics

---

## 📁 Project Structure

```text
AI_Travel_Planner/
│
├── api/
│   ├── gemini_service.py
│   ├── weather_service.py
│   ├── travel_service.py
│   ├── budget_service.py
│   └── pdf_service.py
│
├── database/
│   └── db.py
│
├── data/
│   └── travel_options.csv
│
├── app.py
├── requirements.txt
├── README.md
├── .env
└── travel.db
```

---

## 🚀 Project Development Phases

### Phase 1 — Project Planning

* Define objectives
* Requirement analysis
* Technology selection

Status: ✅ Complete

### Phase 2 — User Interface Development

* Streamlit UI creation
* User input forms
* Layout design

Status: ✅ Complete

### Phase 3 — Gemini AI Integration

* Gemini API configuration
* Prompt engineering
* Dynamic itinerary generation

Status: ✅ Complete

### Phase 4 — Weather API Integration

* OpenWeather API integration
* Live weather display

Status: ✅ Complete

### Phase 5 — Travel Recommendation Module

* Travel suggestions
* Transportation information
* Estimated travel costs

Status: ✅ Complete

### Phase 6 — Budget Analysis

* Expense estimation
* Budget tracking
* Cost breakdown

Status: ✅ Complete

### Phase 7 — Database Integration

* SQLite database creation
* Trip storage
* Travel history management

Status: ✅ Complete

### Phase 8 — PDF Report Generation

* PDF itinerary export
* Download support

Status: ✅ Complete

### Phase 9 — Maps & Analytics

* Google Maps integration
* Travel analytics dashboard

Status: ✅ Complete

### Phase 10 — Deployment Preparation

* GitHub repository management
* Documentation
* Deployment readiness

Status: ✅ Complete

---

## 📊 Project Highlights

* AI-Based Travel Planning
* Personalized Recommendations
* Real-Time Weather Updates
* Budget Optimization
* PDF Report Generation
* SQLite Database Integration
* Analytics Dashboard
* Interactive User Interface

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/srikanthcap/AI_Travel_Planner.git
```

### Navigate to Project Folder

```bash
cd AI_Travel_Planner
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📦 Requirements

```text
streamlit
google-generativeai
python-dotenv
requests
pandas
reportlab
```

---

## 📸 Application Modules

* Home Dashboard
* Weather Information
* Travel Recommendation Engine
* Budget Analysis
* AI Itinerary Generator
* PDF Export
* Trip History
* Analytics Dashboard

---

## 🔮 Future Enhancements

* Flight Booking Integration
* Hotel Booking APIs
* Multi-Language Support
* User Authentication System
* Mobile Application
* AI Cost Optimization
* Travel Recommendation Engine using Machine Learning


## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.

⭐ Star the repository:
https://github.com/srikanthcap/AI_Travel_Planner
