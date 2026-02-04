import requests
import os

def get_news(topic):
    api_key = os.getenv("NEWS_API_KEY")

    if not api_key:
        return ["NEWS_API_KEY not found"]

    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}"
    r = requests.get(url)
    data = r.json()

    if "articles" not in data:
        return ["No news data available"]

    return [a["title"] for a in data["articles"][:3]]
