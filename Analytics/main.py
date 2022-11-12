import streamlit as st
import numpy as np
import pandas as pd
import psycopg2
import altair as alt
import plotly.graph_objects as go
import plotly as pt


# NOTE: This must be the first command in your app, and must be set only once
st.set_page_config(layout="wide")

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])


conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    return pd.read_sql_query(query, conn)


player_df = run_query("SELECT * from player;")

# Header
st.markdown("<h1 style='text-align: center;'>Quiz Game Usage Analytics</h1>", unsafe_allow_html=True)

col1, col2 = st.columns((1, 1))

# First Column
with col1:
    # Top 5 players based on total points
    st.write("Top 5 players based on total points:")

    top5_players = player_df.sort_values(by="total_points", ascending=False).head(5)

    fig=go.Figure(go.Bar(x=top5_players.name, y=top5_players.total_points,
                    hovertemplate =
                    '<b>Player Name</b>: %{x}'+
                    '<br><b>Total Points</b>: %{y}<extra></extra>',))
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=50),
        height=300,
                 )
    st.plotly_chart(fig, use_container_width=True)


# Second Column
with col2:
    df_1 = run_query(
        "SELECT t.category, t.item ->> 'count' AS count, t.item ->> 'points' AS points FROM player, json_each(categories_played) AS t(category, item);"
    )

    # convert column datatype to int datatype
    df_1 = df_1.astype({"count": int, "points": int})

    # Top 5 categories based on total points
    st.write("Top 5 Categories played based on total counts:")

    top_categories = df_1.groupby("category").sum().sort_values(by="count", ascending=False).head(5)

    fig1=go.Figure(go.Bar(x=top_categories.index, y=top_categories["count"],
                        hovertemplate =
                        '<b>Category</b>: %{x}'+
                        '<br><b># Times Played</b>: %{y}<extra></extra>',))
    fig1.update_layout(
        margin=dict(l=0, r=0, t=0, b=50),
        height=300,
                 )
    st.plotly_chart(fig1, use_container_width=True)