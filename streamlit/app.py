# =======================================
# 🧠 Gemini Text Summarizer (Streamlit)
# =======================================

import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    st.error("⚠️ Please add your GEMINI_API_KEY in the .env file.")
    st.stop()

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-pro")

# Streamlit Page Config
st.set_page_config(page_title="AI Text Summarizer", page_icon="🧠", layout="centered")

# Header
st.title("🧠 AI Text Summarizer")
st.markdown("### Powered by Google Gemini API")
st.write("Paste your text below and click **Summarize** to generate a short, meaningful summary.")

# Text Input
text_input = st.text_area("✍️ Enter your text here:", height=250, placeholder="Paste or type your text...")

# Summarize Button
if st.button("✨ Summarize Text"):
    if text_input.strip():
        with st.spinner("Summarizing... Please wait ⏳"):
            try:
                response = model.generate_content(f"Summarize this text concisely and clearly:\n\n{text_input}")
                summary = response.text.strip()
                st.success("✅ Summary Generated Successfully!")
                st.subheader("📜 Summary:")
                st.write(summary)
            except Exception as e:
                st.error(f"⚠️ Error: {str(e)}")
    else:
        st.warning("⚠️ Please enter some text before summarizing.")

# Footer
st.markdown("---")
st.markdown("💡 *Built with Streamlit & Gemini API*")
