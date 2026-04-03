import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("Air Quality Prediction (AQI)")

pm25 = st.number_input("PM2.5")
pm10 = st.number_input("PM10")
no = st.number_input("NO")
no2 = st.number_input("NO2")
so2 = st.number_input("SO2")
co = st.number_input("CO")
o3 = st.number_input("O3")

if st.button("Predict AQI"):
    pm_ratio = pm25 / (pm10 + 1)

    input_data = np.array([[pm25, pm10, no, no2, so2, co, o3, pm_ratio]])
    prediction = model.predict(input_data)

    aqi = prediction[0]

    if aqi <= 50:
        category = "Good"
    elif aqi <= 100:
        category = "Moderate"
    elif aqi <= 200:
        category = "Unhealthy"
    else:
        category = "Very Unhealthy"

    st.success(f"AQI: {aqi:.2f} ({category})")
