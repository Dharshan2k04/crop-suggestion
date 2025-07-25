import streamlit as st
import numpy as np
import sys
import os

# Add the parent directory to the system path to allow importing from app/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.crop_recommendation import predict_crop
from app.weather_api import get_weather_data

st.set_page_config(page_title="Crop Suggestion System", layout="centered")

st.title("🌾 Crop Suggestion System")

st.markdown("This system predicts the most suitable crop to grow based on soil and weather conditions using an LSTM model.")

# Input section
st.header("🧪 Enter Soil Parameters:")
col1, col2, col3 = st.columns(3)
with col1:
    nitrogen = st.number_input("Nitrogen (N)", min_value=0.0, max_value=140.0, value=50.0)
with col2:
    phosphorus = st.number_input("Phosphorus (P)", min_value=0.0, max_value=140.0, value=50.0)
with col3:
    potassium = st.number_input("Potassium (K)", min_value=0.0, max_value=140.0, value=50.0)

# New input for pH
ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0, value=6.5)

st.header("📍 Enter Location for Weather Data")
city = st.text_input("City", value="Tumkur")

if st.button("🔍 Predict Best Crop"):
    with st.spinner("Fetching weather data and predicting..."):
        weather = get_weather_data(city)
        if weather is None:
            st.error("Failed to retrieve weather data. Please try again.")
        else:
            temp = weather["temperature"]
            humidity = weather["humidity"]
            rainfall = weather["rainfall"]

            st.markdown(f"### 🌦️ Weather Info for {city}")
            st.markdown(f"- Temperature: {temp}°C")
            st.markdown(f"- Humidity: {humidity}%")
            st.markdown(f"- Rainfall: {rainfall} mm")

            # Predict crop with ph
            prediction = predict_crop(nitrogen, phosphorus, potassium, temp, humidity, ph, rainfall)


            st.success(f"✅ The most suitable crop to grow is: **{prediction}**")
