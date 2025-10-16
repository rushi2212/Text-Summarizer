from transformers import pipeline

# Load summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


def summarize_text(text):
    summary = summarizer(text, max_length=120, min_length=30, do_sample=False)
    return summary[0]['summary_text']


# Example usage
if __name__ == "__main__":
    text = """
    Climate change is one of the most pressing challenges facing humanity in the 21st century. Rising global temperatures, melting glaciers, and increasing sea levels are direct consequences of human activities, particularly the burning of fossil fuels and deforestation. These changes threaten ecosystems, biodiversity, and human livelihoods across the planet. 

Extreme weather events such as floods, wildfires, hurricanes, and droughts are becoming more frequent and severe, leading to economic losses and displacement of millions of people. Moreover, developing nations are often the hardest hit, despite contributing the least to global emissions. 

To combat climate change, nations must work together to reduce greenhouse gas emissions, invest in renewable energy sources, and promote sustainable practices. Individuals also play a crucial role through lifestyle changes such as reducing waste, conserving energy, and supporting eco-friendly initiatives. 

The time for action is now, as delaying efforts will only worsen the impacts and make adaptation more difficult and costly in the future.

    """
    print("Summary:\n", summarize_text(text))
