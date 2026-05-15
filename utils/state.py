import streamlit as st


def init_session():
    defaults = {
        "chat_history": [],
        "agent_runs": 0,
        "zapier_webhook": "",
        "n8n_webhook": "",
        "website_url": "",
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v
