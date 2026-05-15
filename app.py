"""
AI Marketing Automation Dashboard
Main entry point - Streamlit multi-page app
"""
import streamlit as st
from utils.db import init_db
from utils.state import init_session
from utils.ai import has_key

st.set_page_config(
    page_title="MarketMind AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_db()
init_session()

# ═══════════════════════════════════════════════════════════════
# HEADER
# ═══════════════════════════════════════════════════════════════
st.title("🚀 MarketMind AI Dashboard")
st.caption("Smart marketing automation powered by autonomous AI agents • Gemini API integration")

# Status Bar
website_url = st.session_state.get("website_url", "")
api_status = "✅ API Key Configured" if has_key() else "⚠️ Setup Required"
col_status, col_main = st.columns([1, 4])
with col_status:
    st.markdown(f"**Status:** {api_status}")
with col_main:
    st.text_input(
        "Primary website or landing page URL",
        website_url,
        key="website_url",
        placeholder="https://example.com",
        help="Enter the website URL that should be used as the main marketing context for this dashboard.",
    )

if website_url:
    st.info(f"Using website context: **{website_url}**. AI prompt defaults on SEO and content pages will adapt to this site.")
else:
    st.warning("Enter a website URL above to make this dashboard site-specific.")

st.divider()

# ═══════════════════════════════════════════════════════════════
# KEY METRICS
# ═══════════════════════════════════════════════════════════════
st.subheader("📊 Your Marketing Performance")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Active Campaigns", "12", "+2", delta_color="off")
with col2:
    st.metric("New Leads (24h)", "284", "+18%", delta_color="off")
with col3:
    st.metric("Avg Click Rate", "4.7%", "+0.3%", delta_color="off")
with col4:
    st.metric("AI Agents", "8", "All healthy ✅", delta_color="off")

st.divider()

# ═══════════════════════════════════════════════════════════════
# QUICK START SECTION
# ═══════════════════════════════════════════════════════════════
if not has_key():
    st.error("🔑 **SETUP REQUIRED** — Add your Gemini API key to get started!")
    with st.expander("📋 Setup Instructions (Click to expand)", expanded=True):
        st.markdown("""
        ### Step 1: Get Your Free Gemini API Key
        1. Visit: **[https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)**
        2. Click **"Create API Key"** → **"Create API key in new project"**
        3. Copy the generated key
        
        ### Step 2: Add Key to Your Project
        1. Open `.streamlit/secrets.toml` in the project folder
        2. Paste this line:
        ```toml
        GEMINI_API_KEY = "paste-your-key-here"
        ```
        3. Save and refresh the app (press **F5** or restart the terminal)
        
        ### Step 3: Start Using AI Agents
        - Go to **🤖 AI Agents** to run your first automation
        - Explore **✍️ Content Generator** for AI-powered content
        - Check **📈 Campaign Monitor** for real-time insights
        """)
else:
    st.success("✅ Ready to automate! Start by running agents or generating content.")

st.divider()

# ═══════════════════════════════════════════════════════════════
# FEATURES OVERVIEW
# ═══════════════════════════════════════════════════════════════
st.subheader("🎯 What You Can Do")
col_a, col_b, col_c = st.columns(3)

with col_a:
    st.markdown("### 🤖 AI Agents")
    st.markdown("""
    **Autonomous marketing automation**
    - SEO keyword research
    - Campaign performance analysis
    - Lead scoring & qualification
    - Trend detection & alerts
    """)

with col_b:
    st.markdown("### ✍️ Content Generation")
    st.markdown("""
    **AI-powered content creation**
    - Blog post titles & outlines
    - Ad copy variations
    - Social media captions
    - SEO meta descriptions
    """)

with col_c:
    st.markdown("### 📊 Analytics & Reporting")
    st.markdown("""
    **Real-time insights & reporting**
    - Campaign KPI tracking
    - SEO ranking monitoring
    - Automated reports
    - Trend analysis
    """)

st.divider()

# ═══════════════════════════════════════════════════════════════
# NAVIGATION GUIDE
# ═══════════════════════════════════════════════════════════════
st.subheader("🧭 Quick Navigation")
st.markdown("""
| Feature | Purpose | Start Here |
|---------|---------|-----------|
| 📊 **Dashboard** | View all KPIs at a glance | Homepage |
| 🤖 **AI Agents** | Run autonomous agents | Generate campaigns, keywords, scores |
| 🔍 **SEO Tracker** | Monitor keyword rankings | Track your top keywords |
| 📈 **Campaign Monitor** | Real-time campaign metrics | Check CTR, CPC, conversions |
| 🎯 **Lead Scoring** | AI-powered lead qualification | Filter high-value leads |
| ✍️ **Content Generator** | Create marketing content | Blog, ads, social posts |
| 📑 **Reports** | Auto-generated summaries | Weekly executive reports |
| 💬 **AI Assistant** | Chat with your AI | Ask marketing questions |
| ⚡ **Workflows** | Zapier/N8N automation | Connect external tools |
| ⚙️ **Settings** | Manage configuration | Update API keys |
""")

st.divider()

# ═══════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════
st.caption("© 2026 MarketMind AI • Powered by Google Gemini API • Built with Streamlit")
