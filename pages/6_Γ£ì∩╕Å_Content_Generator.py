# ==============================
# FILE: 6_Content_Generator.py
# ==============================

import streamlit as st

st.title("✍️ AI Content Generator")

website = st.session_state.get("website_url", "")

topic = st.text_input(
    "Content Topic",
    placeholder="AI Marketing Trends"
)

tone = st.selectbox(
    "Content Tone",
    ["Professional", "Marketing", "Technical", "Casual"]
)

if st.button("Generate Content"):

    generated = f"""
# AI Marketing Trends 2026

AI marketing automation is transforming businesses by improving workflow efficiency, SEO monitoring, content generation, and customer engagement.

Website Context: {website}

Benefits:
- Automated SEO monitoring
- AI-generated campaigns
- Real-time reporting
- Smart analytics
"""

    st.text_area("Generated Content", generated, height=300)
