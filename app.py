# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import plotly.express as px

# Sample data
df = pd.DataFrame({
    'Country': ['Finland', 'Denmark', 'India', 'USA', 'Bangladesh'],
    'Happiness Score': [7.8, 7.6, 3.7, 6.9, 4.3],
    'Clothing Waste (kg)': [11.0, 10.5, 4.8, 37.0, 2.1]
})

# Set page config
st.set_page_config(page_title="Happiness vs Fast Fashion", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        .block-container {
            padding: 2rem;
        }
        .styled-box {
            border: 2px solid #00cfff;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            background-color: rgba(255, 255, 255, 0.05);
        }
        .title-text {
            color: #00cfff;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='title-text'>Happiness vs Fast Fashion</h1>", unsafe_allow_html=True)

# Slider filter inside bordered box
with st.container():
    st.markdown("<div class='styled-box'>", unsafe_allow_html=True)
    min_score = st.slider("Show countries with happiness above:", 0.0, 10.0, 5.0)
    filtered_df = df[df['Happiness Score'] > min_score]

    st.write("Filtered Data:")
    st.dataframe(filtered_df)
    st.markdown("</div>", unsafe_allow_html=True)

# Plot inside bordered box
with st.container():
    st.markdown("<div class='styled-box'>", unsafe_allow_html=True)
    fig = px.scatter(filtered_df,
                     x="Clothing Waste (kg)",
                     y="Happiness Score",
                     text="Country",
                     size="Happiness Score",
                     color="Country")
    st.plotly_chart(fig)
    st.markdown("</div>", unsafe_allow_html=True)
