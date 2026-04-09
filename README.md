SkyCast Weather App 

Summary
What it is
A full-stack weather application that displays real-time weather data for any city worldwide, featuring a modern glass-morphism UI and secure API integration.

Tech Stack
Backend: Python Flask with requests library

Frontend: HTML5, CSS3, vanilla JavaScript

API: OpenWeatherMap

Icons: Font Awesome 6.0

Key Features
Search weather by city name

Toggle between Celsius and Fahrenheit units

Displays: temperature, feels like, humidity, wind speed, pressure

Dynamic weather icons

Local time based on city timezone

Responsive design (mobile + desktop)

How it Works
User enters city name in search bar

JavaScript sends request to Flask backend

Flask adds API key and forwards to OpenWeatherMap

Backend filters and returns essential data

Frontend updates UI with weather information

Project Structure
text
weather-app/
├── app.py              # Flask backend
├── requirements.txt    # Python dependencies
├── .env               # API key (hidden)
├── templates/
│   └── index.html     # HTML structure
└── static/
    ├── css/style.css  # Styling
    └── js/weather.js  # Frontend logic
Setup (3 steps)
Install: pip install -r requirements.txt

Add OpenWeatherMap API key to .env file

Run: python app.py

Security
API key stored server-side in .env (never exposed to frontend)

Input validation on all requests

Error Handling
Invalid city names

Network failures

Missing API keys

Server errors

Live Demo Features
Glass-morphism visual design

Loading spinners during API calls

Keyboard support (Enter to search)

Smooth transitions and hover effects

Limitations
Current weather only (no forecast)

Requires internet connection

Free API tier: 60 calls/minute

This is a production-ready weather app template that demonstrates secure API integration, clean code separation, and modern UI/UX practices.
