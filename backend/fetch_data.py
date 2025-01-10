import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("Simple Streamlit App")

# Create a DataFrame
data = pd.DataFrame({
    "x": [1, 2, 3, 4, 5],
    "y": [10, 20, 30, 40, 50]
})

# Plot using Plotly
fig = px.line(data, x="x", y="y", title="Sample Line Chart")

# Display the chart
st.plotly_chart(fig)
