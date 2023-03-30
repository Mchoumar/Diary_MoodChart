import streamlit as st
import plotly.express as px
from organise_data import organise

# recalls the data from organise file
data = organise()

# streamlit website setup
st.title("Diary Tone")

# positive chart
st.subheader("Positivity")
figure1 = px.line(x=data[0], y=data[2], labels={"x": "Dates", "y": "Positivity"})
st.plotly_chart(figure1)

# negative chart
st.subheader("Negativity")
figure2 = px.line(x=data[0], y=data[1], labels={"x": "Dates", "y": "Negativity"})
st.plotly_chart(figure2)