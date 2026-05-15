# ==============================
# FILE: 10_Settings.py
# ==============================

import streamlit as st

st.title("⚙️ Settings")

website = st.session_state.get("website_url", "")

st.markdown("### Current Website")
st.code(website if website else "No website connected")

st.markdown("### API Status")

try:
    from streamlit.runtime.secrets import secrets
    
    if "GEMINI_API_KEY" in secrets:
        st.success("Gemini API Key Connected")
    else:
        st.error("Gemini API Key Missing")

except:
    st.error("Secrets not configured")
