#acts as our frontend 
import streamlit as st
import pandas as pd
import plotly.express as px
from backend.fetch_data import get_crypto_price
from models.anomaly_detection import detect_anomalies

st.title("🚨 Crypto Pump-and-Dump Detection App")

symbol = st.sidebar.text_input("Enter Cryptocurrency Symbol (e.g., bitcoin)", "bitcoin")

if st.button("Check for Pump-and-Dump"):
    try:
        price = get_crypto_price(symbol)
        st.write(f"✅ Current Price of {symbol.capitalize()}: ${price:.2f}")

        historical_prices = [price * (1 + i * 0.01) for i in range(-5, 6)]

        anomalies_df = detect_anomalies(historical_prices)

        st.write("🚩 Detected Anomalies:")
        st.write(anomalies_df[anomalies_df["Anomaly"] == -1])

        fig = px.line(anomalies_df, y="Price", title=f"{symbol.capitalize()} Price Trend with Anomalies")
        fig.add_scatter(y=anomalies_df["Price"][anomalies_df["Anomaly"] == -1], 
                        mode="markers", marker=dict(color="red"), name="Anomaly")
        st.plotly_chart(fig)

    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
