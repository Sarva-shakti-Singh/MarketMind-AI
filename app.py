import streamlit as st
from utils.scraper import scrape_website

st.title("🚀 MarketMind AI")

website = st.text_input(
    "Enter Website URL",
    placeholder="https://example.com"
)

if st.button("Analyze Website"):

    data = scrape_website(website)

    if "error" in data:
        st.error(data["error"])

    else:
        st.success("Website Analyzed Successfully")

        st.session_state.website_data = data

        st.subheader("Website Title")
        st.write(data["title"])

        st.subheader("Headings")
        st.write(data["headings"])

        st.subheader("Content Preview")
        st.write(data["content"][:1000])
