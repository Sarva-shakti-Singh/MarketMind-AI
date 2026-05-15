import streamlit as st
from agents.marketing_agents import AGENTS
from utils.db import fetch_df, init_db
from utils.state import init_session

init_db(); init_session()
st.title("🤖 Autonomous AI Agents")
st.caption("Run AI agents on demand or via scheduled workflows (N8N/Zapier).")

for name, (desc, fn, needs_input) in AGENTS.items():
    with st.expander(f"**{name}** — {desc}"):
        if needs_input:
            val = st.text_input(f"Input for {name}", key=f"in_{name}",
                                placeholder="e.g. MarketMind AI")
            if st.button(f"▶ Run {name}", key=f"btn_{name}"):
                with st.spinner("Agent working..."):
                    result = fn(val or "marketing")
                if isinstance(result, tuple):
                    st.success(result[0]); st.markdown(result[1])
                else:
                    st.markdown(result)
        else:
            if st.button(f"▶ Run {name}", key=f"btn_{name}"):
                with st.spinner("Agent working..."):
                    result = fn()
                if isinstance(result, tuple):
                    st.success(result[0]); st.markdown(result[1])
                else:
                    st.markdown(result)

st.divider()
st.subheader("📋 Agent Activity Log")
logs = fetch_df("SELECT agent,status,message,created_at FROM agent_logs ORDER BY id DESC LIMIT 30")
st.dataframe(logs, use_container_width=True)
