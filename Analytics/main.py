import streamlit as st
import numpy as np
import pandas as pd
import psycopg2
import altair as alt

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

col1, col2 = st.columns((1,1))

# First Column
with col1:
    df = run_query("SELECT * from player;")

    # Top 5 players based on total points
    st.write("Top 5 players based on total points:")
    st.bar_chart(
        df.sort_values(by="total_points", ascending=False).head(5),
        x="name",
        y="total_points",
    )

# Second Column
with col2:
    df_1 = run_query("SELECT t.category, t.item ->> 'count' AS count, t.item ->> 'points' AS points FROM player, json_each(categories_played) AS t(category, item);")

    # convert column datatype to int datatype
    df_1 = df_1.astype({"count": int, "points": int})

    # Top 5 categories based on total points
    st.write("Top 5 Categories played based on total counts:")
    st.bar_chart(
        df_1.groupby("category").sum().sort_values(by="count", ascending=False).head(5),
        y="count",
    )