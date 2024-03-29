import streamlit as st
import numpy as np
import pandas as pd
import psycopg2
import altair as alt
from datetime import datetime
import calendar
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

# Header
st.markdown("<h1 style='text-align: center;'>Quiz Game Usage Analytics</h1>", unsafe_allow_html=True)
st.markdown('#')

# Workings for Top 5 Players based on Total Points
player_df = run_query("SELECT * from player;")
top5_players = player_df.sort_values(by="total_points", ascending=False).head(5)

# Workings for Top 5 Categories and Top 5 Quizzes Based on Number of Times Played

df_1 = run_query(
    "SELECT name, categories_played FROM player;"
)

user_data = []
display_user_data = []
def extract_json(row):
    user_name = row["name"]
    user_dict = row["categories_played"]
    
    for category, value_dict in user_dict.items():
        for quiz, item in value_dict.items():
            # st.write(user_id, quiz)
            row_list = [user_name, category, quiz, item["count"], item["points"]]
            # st.write(row_list)
            row_list1 = [category, quiz, item["count"]]
            user_data.append(row_list)
            display_user_data.append(row_list1)
        
    return

df_1.apply(lambda row: extract_json(row), axis=1)
user_df = pd.DataFrame(user_data)
display_user_df = pd.DataFrame(display_user_data)
user_df.columns = ["name", "category", "quiz", "count", "points"]
display_user_df.columns = ["Quiz Category", "Quiz Title", "Number of Times Played"]

# convert column datatype to int datatype
user_df = user_df.astype({"count": int, "points": int})
display_user_df = display_user_df.astype({'Number of Times Played':int})

top_categories = user_df.groupby("category").sum().sort_values(by="count", ascending=False).head(5)
top_quizzes = user_df.groupby("quiz").sum().sort_values(by="count", ascending=False).head(5)
display_user_df = display_user_df.groupby(["Quiz Category", "Quiz Title"]).sum().sort_values(by="Number of Times Played", ascending=False).reset_index()
# display_user_df.columns = ["Quiz Category", "Quiz Title", "Number of Times Played"]

# Workings for Average duration of quizzes played over time
duration_df = run_query("SELECT id, start_times, end_times from player;")
def change_datetime(time_array):
    duration_list = []
    if time_array == None:
        return duration_list
    else:
        for cell in time_array:
            duration_list.append(datetime.strptime(cell,"%Y-%m-%dT%H:%M:%S"))
        
        return duration_list

def clean_time_df(duration_df):
    duration_df["start_times"] = duration_df["start_times"].apply(lambda x: change_datetime(x))
    duration_df["end_times"] = duration_df["end_times"].apply(lambda x: change_datetime(x))
    return duration_df

duration_df = clean_time_df(duration_df)

log_list = []

def get_duration(row, total=False):
    start_array = row["start_times"]
    end_array = row["end_times"]

    duration_list = []
    for i in range(len(start_array)):

        start = start_array[i]
        end = end_array[i]
        duration = (end-start).total_seconds() / 60
        duration_list.append(duration)
    
    if total:
        return {row["id"]: sum(duration_list)}
    else:
        global log_list
        for j in range(len(duration_list)):
            log_list.append([start_array[j],duration_list[j]])
        return log_list

duration_output = []
duration_output.append(duration_df.apply(lambda row: get_duration(row,total=True), axis=1))

duration_df.apply(lambda row: get_duration(row), axis=1)
col_list = ["date","duration"]
log_df = pd.DataFrame(log_list, columns= col_list)


# Workings for the 3 Metrics
unique_players = player_df["id"].count()
total_quizzes_played = sum(top_categories["count"])
log_df = log_df.groupby(log_df['date'].dt.date)['duration'].mean()
new_sum = sum(log_df)/log_df.count()

# PLOTTING 3 METRICS
col1, col2, col3 = st.columns(3, gap="large")
col1.metric("Total number of unique players so far", unique_players)
col2.metric("Total number of quizzes played so far", total_quizzes_played)
col3.metric("Average duration of quizzes played (in mins)", round(new_sum,2))
st.markdown('#')


col1, col2 = st.columns((1, 1), gap="large")
# PLOTTING TOP 5 PLAYERS BASED ON TOTAL POINTS
with col1:
    st.subheader("Top 5 Players based on Total Points")
    fig=go.Figure(go.Bar(x=top5_players.name, y=top5_players.total_points,
                    hovertemplate =
                    '<b>Player Name</b>: %{x}'+
                    '<br><b>Total Points</b>: %{y}<extra></extra>',))
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=50),
        height=300,
                 )
    fig.update_xaxes(title_text='Player Name')
    fig.update_yaxes(title_text='Total Points')
    st.plotly_chart(fig, use_container_width=True)


# PLOTTING TOP 5 CATEGORIES BASED ON NUMBER OF TIMES PLAYED
with col2:
    st.subheader("Top 5 Categories based on Number of Times Played")
    fig1=go.Figure(go.Bar(x=top_categories.index, y=top_categories["count"],
                        hovertemplate =
                        '<b>Category</b>: %{x}'+
                        '<br><b># Times Played</b>: %{y}<extra></extra>',))
    fig1.update_layout(
        margin=dict(l=0, r=0, t=0, b=50),
        height=300,
        )
    fig1.update_xaxes(title_text='Category Name')
    fig1.update_yaxes(title_text='Number of Times Played')
    st.plotly_chart(fig1, use_container_width=True)



col3, col4 = st.columns((1, 1), gap="large")
# PLOTTING TOP 5 QUIZZES BASED ON NUMBER OF TIMES PLAYED
with col3:
    st.subheader("Top 5 Quizzes based on Number of Times Played")
    fig2=go.Figure(go.Bar(x=top_quizzes.index, y=top_quizzes["count"],
                        hovertemplate =
                        '<b>Quiz</b>: %{x}'+
                        '<br><b># Times Played</b>: %{y}<extra></extra>',))
    fig2.update_layout(
        margin=dict(l=0, r=0, t=0, b=50),
        height=300,
        )
    fig2.update_xaxes(title_text='Quiz Title')
    fig2.update_yaxes(title_text='Number of Times Played')
    st.plotly_chart(fig2, use_container_width=True)

with col4:
    st.subheader("Quiz Game Statistics")
    st.dataframe(display_user_df, height=250, use_container_width=True)
    st.caption("This table is scrollable.")


# PLOTTING THE AVERAGE DURATION OF QUIZZES PLAYED OVER TIME GRAPH 
st.subheader("Average Duration of Quizzes Played Over Time")

year_period = [2022, 2023, 2024]
year_option = st.selectbox(
    'Select the Year:',
    year_period
)

month_name = list(calendar.month_name)[1:]
months_choices = {}
for i in range(1,13):
    months_choices[month_name[i-1]] = i

month_option = st.selectbox(
    'Select the Month:',
    month_name
)


log_df = pd.DataFrame(log_list, columns= col_list)
log_df = log_df[log_df["date"].dt.year == year_option]

log_df = log_df[log_df["date"].dt.month == months_choices[month_option]]


mean_duration = log_df.groupby([log_df['date'].dt.date])['duration'].mean()
mean_df = pd.DataFrame(mean_duration)

mean_df = mean_df.reset_index()
mean_df["date"] = pd.to_datetime(mean_df["date"])
mean_df["day"] = mean_df["date"].dt.day

# st.line_chart(mean_df, x="day", y="duration")
fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=mean_df["day"], y=mean_df["duration"],
                    hovertemplate =
                        '<b>Day</b>: %{x} '+ month_option +
                        '<br><b>Avg Duration Played</b>: %{y} minutes <extra></extra>',))
fig3.update_layout(
        margin=dict(l=0, r=0, t=0, b=50),
        height=375,
        )
fig3.update_xaxes(title_text='Day')
fig3.update_yaxes(title_text='Average Duration Played (in minutes)')


def check_avail(mean_df):
    if mean_df.empty:
        st.write('*There were no quizzes played in', month_option, str(year_option), '.', 'Please select another month.')
    else:
        st.plotly_chart(fig3, use_container_width=True)
        avg_duration_per_month = sum(mean_df['duration'])/len(mean_df)
        st.write('The total average duration of quizzes played in', month_option, str(year_option), 'is:', round(avg_duration_per_month,2), 'minutes')

check_avail(mean_df)
