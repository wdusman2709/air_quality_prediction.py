import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("Air Quality Index Prediction")

pm25 = st.number_input("PM2.5")
pm10 = st.number_input("PM10")
no = st.number_input("NO")
no2 = st.number_input("NO2")
so2 = st.number_input("SO2")
co = st.number_input("CO")
o3 = st.number_input("O3")

if st.button("Predict AQI"):
    pollution_index = (pm25 + pm10 + no2) / 3

    input_data = np.array([[pm25, pm10, no, no2, so2, co, o3, pollution_index]])
    prediction = model.predict(input_data)

    st.success(f"Predicted AQI: {prediction[0]:.2f}")
