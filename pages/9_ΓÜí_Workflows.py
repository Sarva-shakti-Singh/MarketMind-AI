import streamlit as st
import requests
from datetime import datetime
from utils.state import init_session
from utils.db import log_agent, init_db

init_db(); init_session()
st.title("⚡ Workflow Automation")
st.caption("Trigger N8N or Zapier workflows via webhooks.")

st.subheader("🔗 Webhook URLs")
st.session_state.zapier_webhook = st.text_input(
    "Zapier Webhook URL", st.session_state.zapier_webhook,
    placeholder="https://hooks.zapier.com/hooks/catch/...")
st.session_state.n8n_webhook = st.text_input(
    "N8N Webhook URL", st.session_state.n8n_webhook,
    placeholder="https://your-n8n.com/webhook/...")

st.divider()
st.subheader("🚀 Trigger Workflow")
target = st.radio("Target", ["Zapier", "N8N"])
event = st.selectbox("Event type", [
    "new_lead", "campaign_alert", "weekly_report", "seo_alert", "content_published"
])
payload_text = st.text_area("Payload (JSON)",
                            '{"source": "ai-marketing-dashboard", "priority": "high"}')

if st.button("⚡ Fire webhook"):
    url = st.session_state.zapier_webhook if target == "Zapier" else st.session_state.n8n_webhook
    if not url:
        st.error(f"Set the {target} webhook URL above first.")
    else:
        import json
        try:
            payload = json.loads(payload_text)
        except Exception:
            payload = {"raw": payload_text}
        payload.update({"event": event, "timestamp": datetime.now().isoformat()})
        try:
            r = requests.post(url, json=payload, timeout=10)
            st.success(f"✅ Sent ({r.status_code})")
            log_agent("Workflow", "success", f"{target} {event} → {r.status_code}")
        except Exception as e:
            st.error(f"❌ {e}")
            log_agent("Workflow", "error", str(e))

st.divider()
st.subheader("📚 Setup Guide")
st.markdown("""
**Zapier:** Create a Zap → Trigger: *Webhooks by Zapier (Catch Hook)* → copy URL → paste above.

**N8N:** Add a *Webhook* node → set HTTP method POST → copy production URL → paste above.

**Recommended automations:**
- New high-value lead → Slack alert + CRM update
- Weekly report → Email to team
- SEO alert (rank drop) → Notification + Trello card
- Campaign anomaly → PagerDuty / Discord
""")
