"""Gemini AI wrapper with graceful fallback when no API key is configured."""
import streamlit as st
import os


def get_api_key():
    try:
        return st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY", "")
    except Exception:
        return os.getenv("GEMINI_API_KEY", "")


def has_key():
    return bool(get_api_key())


def generate(prompt: str, system: str = "", model: str = "gemini-2.0-flash") -> str:
    key = get_api_key()
    if not key:
        return ("⚠️ No Gemini API key configured. Add `GEMINI_API_KEY` to "
                "`.streamlit/secrets.toml` (see `secrets.toml.example`).\n\n"
                f"**Prompt was:**\n{prompt[:500]}")
    try:
        import google.generativeai as genai
        genai.configure(api_key=key)
        m = genai.GenerativeModel(model, system_instruction=system or None)
        resp = m.generate_content(prompt)
        return resp.text or "(empty response)"
    except Exception as e:
        return f"❌ AI error: {e}"


def chat(messages, system: str = "You are a senior AI marketing strategist.") -> str:
    key = get_api_key()
    if not key:
        last = messages[-1]["content"] if messages else ""
        return f"⚠️ No Gemini API key configured. Echo: {last}"
    try:
        import google.generativeai as genai
        genai.configure(api_key=key)
        m = genai.GenerativeModel("gemini-2.0-flash", system_instruction=system)
        history = []
        for msg in messages[:-1]:
            history.append({"role": "user" if msg["role"] == "user" else "model",
                            "parts": [msg["content"]]})
        chat_session = m.start_chat(history=history)
        resp = chat_session.send_message(messages[-1]["content"])
        return resp.text or "(empty response)"
    except Exception as e:
        return f"❌ AI error: {e}"
