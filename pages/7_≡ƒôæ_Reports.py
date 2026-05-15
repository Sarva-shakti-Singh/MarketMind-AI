import streamlit as st
from utils.db import fetch_df, init_db
from utils.state import init_session
from agents.marketing_agents import report_agent

init_db(); init_session()
st.title("📑 Automated Reports")

if st.button("🤖 Generate New Weekly Report"):
    with st.spinner("AI compiling report..."):
        title, content = report_agent()
    st.success(f"Generated: {title}")

reports = fetch_df("SELECT id,title,created_at FROM reports ORDER BY id DESC")
st.subheader("Saved Reports")
if reports.empty:
    st.info("No reports yet. Generate one above.")
else:
    for _, r in reports.iterrows():
        with st.expander(f"📄 {r['title']}  •  {r['created_at']}"):
            row = fetch_df("SELECT content FROM reports WHERE id=?", (int(r["id"]),))
            content = row.iloc[0]["content"]
            st.markdown(content)
            st.download_button("⬇ Download (.md)", content,
                               file_name=f"{r['title']}.md", key=f"dl_{r['id']}")
