# ==============================
# FILE: state.py
# ==============================

import streamlit as st

def init_state():
    defaults = {
        "website_url": "",
        "gemini_api_key": "",
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
