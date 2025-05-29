import wikipedia

def fetch_summary(topic: str, sentences=5) -> str:
    try:
        summary = wikipedia.summary(topic, sentences=sentences)
        return summary
    except Exception as e:
        return f"Error fetching Wikipedia content: {str(e)}"
