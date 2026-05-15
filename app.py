# ==============================
# FILE: app.py
# ==============================

import streamlit as st
from state import init_state

st.set_page_config(
    page_title="MarketMind AI",
    page_icon="🚀",
    layout="wide"
)

init_state()

st.title("🚀 MarketMind AI")
st.subheader("AI Marketing Automation Dashboard")

st.markdown("### Website Configuration")

website = st.text_input(
    "Enter Website URL",
    placeholder="https://yourwebsite.com"
)

if website:
    st.session_state.website_url = website
    st.success(f"Connected to: {website}")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("SEO Score", "87%")

with col2:
    st.metric("Campaign Health", "92%")

with col3:
    st.metric("AI Agents Active", "6")

st.markdown("---")

st.markdown("""
### Features
- AI SEO Monitoring
- Content Generation
- Campaign Tracking
- AI Marketing Agents
- Automated Reports
- Real-Time Analytics
""")
