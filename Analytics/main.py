import streamlit as st
import numpy as np
import pandas as pd
import psycopg2
import altair as alt

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


df = run_query("SELECT * from player;")

# Top 5 players based on total points
st.write("Top 5 players based on total points:")
st.bar_chart(
    df.sort_values(by="total_points", ascending=False).head(5),
    x="name",
    y="total_points",
)
