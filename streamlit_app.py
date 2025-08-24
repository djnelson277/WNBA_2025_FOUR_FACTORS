import streamlit as st
import pandas as pd
import plotly.express as px

#Load the dataset
df = pd.read_csv('wnba_2025_predictions.csv')


# Melt the dataframe for Plotly
df_melted = df.melt(id_vars='TEAM_NAME', 
                    value_vars=['W', 'Predicted Wins'],
                    var_name='Metric', 
                    value_name='Wins')

# Create the bar chart with column references
fig = px.bar(
    df_melted,
    x='TEAM_NAME',
    y='Wins',  # Now matches melted column name
    color='Metric',
    barmode='group',
    title='WNBA Team Performance: Actual vs Predicted Wins',
    color_discrete_map={
        'W': '#FFA500',  # Orange for actual wins
        'Predicted Wins': '#1F77B4'  # Blue for predicted
    },
    text='Wins'
)

# Rest of your layout customization...
fig.update_layout(
    yaxis_title='Number of Wins',
    xaxis_title='',
    legend_title='',
    height=500
)

st.plotly_chart(fig, use_container_width=True)