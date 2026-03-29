import streamlit as st
import pandas as pd
import joblib

# Load model and columns
model = joblib.load("crop_model.pkl")
columns = joblib.load("columns.pkl")

st.set_page_config(page_title="AI Farmer Assistant", layout="centered")

st.title("🌾 AI Farmer Assistant")
st.write("Get crop recommendation based on soil and weather conditions")

# Input fields
n = st.number_input("Nitrogen (N)", min_value=0)
p = st.number_input("Phosphorus (P)", min_value=0)
k = st.number_input("Potassium (K)", min_value=0)
temp = st.number_input("Temperature (°C)")
humidity = st.number_input("Humidity (%)")
ph = st.number_input("pH value")
rainfall = st.number_input("Rainfall (mm)")

# Predict button
if st.button("🌱 Predict Crop"):

    input_data = pd.DataFrame([[n, p, k, temp, humidity, ph, rainfall]],
                              columns=columns)

    prediction = model.predict(input_data)

    st.success(f"✅ Recommended Crop: {prediction[0]}")

    # Explanation (basic)
    st.info("🌟 Recommendation is based on soil nutrients and environmental conditions.")