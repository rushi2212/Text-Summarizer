import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize model
model = genai.GenerativeModel("gemini-2.5-flash")

def summarize_text(text):
    prompt = f"Summarize the following text in a concise and clear way:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text.strip()

if __name__ == "__main__":
    text = input("Enter text to summarize:\n\n")
    
    if text.strip():
        summary = summarize_text(text)
        print("\n📝 Summary:\n", summary)
    else:
        print("⚠️ No text entered.")
