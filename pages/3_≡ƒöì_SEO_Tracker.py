import streamlit as st
import plotly.express as px
from urllib.parse import urlparse
from utils.db import fetch_df, get_conn, init_db
from utils.state import init_session
from agents.marketing_agents import keyword_research_agent, seo_trend_agent
from datetime import datetime
import random

init_db(); init_session()
website_url = st.session_state.get("website_url", "")
hostname = ""
if website_url:
    parsed = urlparse(website_url)
    hostname = parsed.hostname or website_url

st.title("🔍 SEO Tracking System")
if website_url:
    st.caption(f"SEO context set for {hostname}")

kws = fetch_df("SELECT * FROM keywords ORDER BY rank")

c1, c2, c3 = st.columns(3)
c1.metric("Tracked Keywords", len(kws))
c2.metric("Avg Rank", f"{kws['rank'].mean():.1f}")
c3.metric("Top 10 Rankings", int((kws['rank'] <= 10).sum()))

st.subheader("Keyword Rankings")
st.dataframe(kws, use_container_width=True)

st.plotly_chart(px.scatter(kws, x="volume", y="rank", size="difficulty",
                           color="trend", hover_name="keyword",
                           title="Volume vs Rank (size = difficulty)"),
                use_container_width=True)

st.divider()
st.subheader("➕ Add / Track New Keyword")
with st.form("addkw"):
    new_kw = st.text_input("Keyword")
    if st.form_submit_button("Track"):
        if new_kw.strip():
            conn = get_conn()
            conn.execute("INSERT INTO keywords(keyword,volume,difficulty,rank,trend,updated_at) VALUES(?,?,?,?,?,?)",
                         (new_kw, random.randint(500, 30000), random.randint(20, 90),
                          random.randint(1, 80), random.choice(["↑", "↓", "→"]),
                          datetime.now().isoformat()))
            conn.commit(); conn.close()
            st.success(f"Now tracking '{new_kw}'"); st.rerun()

st.divider()
st.subheader("🤖 AI Keyword Research")
seed_default = hostname if hostname else "ai marketing automation"
seed = st.text_input("Seed keyword", seed_default)
if st.button("Research"):
    with st.spinner("AI researching..."):
        st.markdown(keyword_research_agent(seed))

st.subheader("📈 AI SEO Trend Analysis")
topic_default = f"SEO strategy for {hostname}" if hostname else "marketing automation 2025"
topic = st.text_input("Topic", topic_default)
if st.button("Analyze trends"):
    with st.spinner("AI analyzing..."):
        st.markdown(seo_trend_agent(topic))
