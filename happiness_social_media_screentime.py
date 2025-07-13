import streamlit as st
import pandas as pd
import plotly.express as px

happiness_df=pd.read_excel(r'C:\Users\Admin\Desktop\New folder\Dashboard_ambitous_project\happiness-vs-fastfashion\data\WHR24_Data_Figure_2.1.xls')
socialmediatime_df=pd.read_csv(r'C:\Users\Admin\Desktop\New folder\Dashboard_ambitous_project\happiness-vs-fastfashion\data\social-media-timespent-by-country.csv')
# print(social_media_df)

# Perform inner join
merged_df = pd.merge(
    happiness_df,
    socialmediatime_df,
    on='country',
    how='inner'
)

# View result
# print(merged_df)
# print(merged_df.columns)

st.title("Happiness vs Social Media time spent by Country")

# Scatter plot
fig = px.scatter(
    merged_df,
    x='Time_Spent_using_Social_Media',
    y='Ladder score',
    size='Ladder score',             # Optional: bubble size
    color='country',                 # Optional: color by country
    hover_name='country',            # Hover to show country name
    title='Happiness Score vs % Social Media time usage (2024)'
)

st.plotly_chart(fig)

