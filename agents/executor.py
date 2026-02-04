from tools.weather_tool import get_weather
from tools.news_tool import get_news

def executor(plan):
    results = {}

    for step in plan:
        if step["tool"] == "weather":
            results["weather"] = get_weather(step["input"])

        if step["tool"] == "news":
            results["news"] = get_news(step["input"])

    return results
