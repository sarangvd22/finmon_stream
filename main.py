import streamlit as st
import pandas as pd
import plotly.express as px

from streamlit_plotly_events import plotly_events


st.write("""
# Financial Monitor
""")

df = pd.read_csv("finmon_bse.csv")
#my_df = df[['index_date','close']]
df.index_date = pd.to_datetime(df.index_date, format="%d-%b-%Y")
df.sort_values(by="index_date", ascending=True)

#st.line_chart(data=my_df, x='index_date', y='close')

# Create plotly line graph
fig = px.line(data_frame=df, x=df.index_date, y=df.close, line_group=df.index_name, color=df.index_name)
fig.update_traces(mode="lines", hovertemplate="%{y:,.2f}")
fig.update_layout(hovermode="x unified")
selected_points = plotly_events(fig, click_event=False, hover_event=True)

