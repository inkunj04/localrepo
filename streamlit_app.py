import streamlit as st
import joblib
import numpy as np

model = joblib.load('calories_model.pkl')

st.title("Calories Burnt Predictor")

gender = st.radio("Gender", ['Male', 'Female'])
age = st.number_input("Age", min_value=10, max_value=100)
height = st.number_input("Height (cm)")
weight = st.number_input("Weight (kg)")
duration = st.number_input("Exercise Duration (minutes)")
heart_rate = st.number_input("Heart Rate")
body_temp = st.number_input("Body Temperature (°C)")

gender = 0 if gender == 'Male' else 1

input_data = np.array([[gender, age, height, weight, duration, heart_rate, body_temp]])
prediction = model.predict(input_data)

st.success(f"Predicted Calories Burnt: {prediction[0]:.2f}")


