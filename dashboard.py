import streamlit as st
from weather import get_weather
from predictor import predict
from trader import paper_trade

st.title("🌦️ Weather AI Agent")

cities = ["Delhi", "Mumbai", "London", "Tokyo", "New York"]

city = st.selectbox("Select City", cities)

if st.button("Predict"):

    weather = get_weather(city)
    result = predict(weather)
    balance = paper_trade(result["trade"])

    st.subheader("Prediction")

    st.write(result)

    st.success(f"Paper Trade Balance : ₹{balance}")