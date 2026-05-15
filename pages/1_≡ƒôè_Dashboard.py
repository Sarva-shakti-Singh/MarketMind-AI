import streamlit as st
import pandas as pd
import plotly.express as px
from utils.db import fetch_df, init_db
from utils.state import init_session

init_db(); init_session()
st.title("📊 Real-Time Marketing Dashboard")

camps = fetch_df("SELECT * FROM campaigns")
leads = fetch_df("SELECT * FROM leads")
kws = fetch_df("SELECT * FROM keywords")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Spend", f"${camps['spend'].sum():,.0f}")
c2.metric("Total Conversions", int(camps['conversions'].sum()))
c3.metric("Avg CTR", f"{camps['ctr'].mean():.2f}%")
c4.metric("Total Leads", len(leads))

st.subheader("Spend by Channel")
fig = px.bar(camps.groupby("channel", as_index=False)["spend"].sum(),
             x="channel", y="spend", color="channel")
st.plotly_chart(fig, use_container_width=True)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Conversion Rate by Campaign")
    st.plotly_chart(px.bar(camps.sort_values("conv_rate", ascending=False).head(10),
                           x="name", y="conv_rate", color="channel"), use_container_width=True)
with col2:
    st.subheader("Lead Distribution")
    st.plotly_chart(px.pie(leads, names="category", title=None), use_container_width=True)

st.subheader("Top Keywords")
st.dataframe(kws.sort_values("rank").head(10), use_container_width=True)

st.subheader("Campaign Table")
st.dataframe(camps, use_container_width=True)
