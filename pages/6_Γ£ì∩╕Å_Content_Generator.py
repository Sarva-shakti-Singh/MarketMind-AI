import streamlit as st
from urllib.parse import urlparse
from utils.ai import generate
from utils.state import init_session

init_session()
website_url = st.session_state.get("website_url", "")
hostname = ""
if website_url:
    parsed = urlparse(website_url)
    hostname = parsed.hostname or website_url

st.title("✍️ AI Content Generator")
if website_url:
    st.caption(f"Writing content for {hostname}")

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["Blog Titles", "Ad Copy", "SEO Meta", "Social Captions", "Full Blog Post"]
)

with tab1:
    default_topic = f"AI marketing automation for {hostname}" if hostname else "AI marketing automation"
    topic = st.text_input("Topic", default_topic, key="t1")
    n = st.slider("How many", 5, 20, 10)
    if st.button("Generate", key="b1"):
        st.markdown(generate(f"Generate {n} viral, SEO-friendly blog titles about '{topic}'.",
                             "You are a top-tier content strategist."))

with tab2:
    product = st.text_input("Product/Service", f"{hostname} marketing platform" if hostname else "AI marketing dashboard")
    audience = st.text_input("Audience", "growth marketers")
    platform = st.selectbox("Platform", ["Google Ads", "Facebook", "LinkedIn", "TikTok"])
    if st.button("Generate", key="b2"):
        st.markdown(generate(
            f"Write 5 high-converting {platform} ad variants for '{product}' targeting {audience}. "
            "Include headline, primary text, CTA for each.",
            "You are a direct-response copywriter."))

with tab3:
    page = st.text_input("Page topic", f"{hostname} homepage copy" if hostname else "AI marketing automation platform", key="t3")
    if st.button("Generate", key="b3"):
        st.markdown(generate(
            f"Generate 5 SEO meta description options (max 160 chars each) for a page about '{page}'. "
            "Include the keyword naturally and a CTA.",
            "You are an SEO copywriter."))

with tab4:
    topic4 = st.text_input("Topic", f"launching {hostname}'s new AI marketing platform" if hostname else "launching our AI marketing platform", key="t4")
    if st.button("Generate", key="b4"):
        st.markdown(generate(
            f"Write social media captions for '{topic4}' for: LinkedIn (professional), "
            "Instagram (engaging + emojis), X/Twitter (punchy <280 chars), TikTok (Gen-Z hook).",
            "You are a social media manager."))

with tab5:
    topic5 = st.text_input("Topic", f"How {hostname} uses AI agents to automate marketing" if hostname else "How AI agents automate marketing", key="t5")
    if st.button("Generate full post", key="b5"):
        with st.spinner("Writing..."):
            st.markdown(generate(
                f"Write a 600-word SEO-optimized blog post about '{topic5}'. Include H2 sections, "
                "intro hook, bullet points, conclusion with CTA.",
                "You are an expert content writer."))
