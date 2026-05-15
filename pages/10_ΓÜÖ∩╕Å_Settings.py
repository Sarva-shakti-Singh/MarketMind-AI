import streamlit as st
import os
from utils.ai import has_key
from utils.state import init_session

init_session()
st.title("⚙️ Settings")

website_url = st.session_state.get("website_url", "")
st.subheader("🌐 Current Website")
if website_url:
    st.success(f"Using website URL: {website_url}")
else:
    st.info("No website URL selected yet. Set one on the dashboard homepage.")

st.subheader("🔑 API Keys")
if has_key():
    st.success("✅ Gemini API key configured")
else:
    st.error("❌ No Gemini API key. Add `GEMINI_API_KEY` to `.streamlit/secrets.toml`.")
    st.code('GEMINI_API_KEY = "your-key-here"', language="toml")
    st.markdown("Get a free key: https://aistudio.google.com/apikey")

st.subheader("🗄 Database")
db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "marketing.db")
st.code(db_path)
if os.path.exists(db_path):
    st.caption(f"Size: {os.path.getsize(db_path)/1024:.1f} KB")

st.subheader("🔄 Reset Demo Data")
if st.button("⚠️ Delete database & reseed on next run"):
    if os.path.exists(db_path):
        os.remove(db_path)
        st.success("Deleted. Refresh the app to reseed.")

st.subheader("🧩 Optional Integrations")
st.markdown("""
You can extend this platform by adding API keys to `.streamlit/secrets.toml`:
- `OPENAI_API_KEY` — alternative LLM
- `GOOGLE_ADS_API_KEY` — pull live campaign data
- `SERP_API_KEY` — real keyword rankings
- `HUBSPOT_API_KEY` / `SALESFORCE_API_KEY` — CRM sync
- `SENDGRID_API_KEY` / `MAILGUN_API_KEY` — email automation
""")
