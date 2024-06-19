import streamlit as st
import plotly.express as px
import sqlite3
import pandas as pd

# Create a SQL connection to our SQLite database and read sqlite query results into a pandas DataFrame
con = sqlite3.connect("files/data.db")
df = pd.read_sql_query("SELECT * from temp", con)
cur = con.cursor()

# Display data on graph
figure = px.line(x=df["date"], y=df["temperature"],
                             labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)

# Close the connection
con.close()
