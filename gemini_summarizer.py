import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

def summarize_text(text):
    prompt = f"Summarize the following text in a concise and clear way:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text.strip()

# Example usage
if __name__ == "__main__":
    text = """
    Artificial intelligence (AI) is a rapidly advancing field that focuses on creating systems capable of performing tasks 
    that typically require human intelligence. These tasks include understanding language, recognizing patterns, solving 
    problems, and learning from experience. AI has applications in healthcare, education, finance, and more.
    """
    summary = summarize_text(text)
    print("Summary:\n", summary)
