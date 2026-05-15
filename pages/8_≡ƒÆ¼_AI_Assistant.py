import streamlit as st
from utils.ai import chat
from utils.state import init_session

init_session()
st.title("💬 AI Marketing Assistant")
st.caption("Ask anything about your campaigns, SEO, content, leads, or strategy.")

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask your marketing AI..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            reply = chat(st.session_state.chat_history)
        st.markdown(reply)
    st.session_state.chat_history.append({"role": "assistant", "content": reply})

if st.session_state.chat_history and st.button("🗑 Clear chat"):
    st.session_state.chat_history = []; st.rerun()
