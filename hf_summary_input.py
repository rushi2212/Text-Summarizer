from transformers import pipeline

# Load summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    summary = summarizer(text, max_length=120, min_length=30, do_sample=False)
    return summary[0]['summary_text']

if __name__ == "__main__":
    text = input("Enter text to summarize:\n\n")
    
    if text.strip():
        summary = summarize_text(text)
        print("\n📝 Summary:\n", summary)
    else:
        print("⚠️ No text entered.")
