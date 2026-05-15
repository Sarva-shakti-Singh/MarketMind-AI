import streamlit as st
import plotly.express as px
from utils.db import fetch_df, init_db
from utils.state import init_session
from agents.marketing_agents import lead_scoring_agent

init_db(); init_session()
st.title("🎯 AI Lead Scoring Engine")

leads = fetch_df("SELECT * FROM leads ORDER BY score DESC")

c1, c2, c3 = st.columns(3)
c1.metric("High-value", int((leads['category'] == "High").sum()))
c2.metric("Medium", int((leads['category'] == "Medium").sum()))
c3.metric("Low", int((leads['category'] == "Low").sum()))

st.plotly_chart(px.histogram(leads, x="score", color="category", nbins=20),
                use_container_width=True)

st.plotly_chart(px.pie(leads, names="source", title="Lead Sources"),
                use_container_width=True)

if st.button("🤖 Re-score all leads with AI"):
    st.success(lead_scoring_agent()); st.rerun()

st.subheader("All Leads")
st.dataframe(leads, use_container_width=True)
