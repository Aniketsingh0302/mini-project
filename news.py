import requests
import json

query= input("enter the topic of the news--")
url =(f"https://newsapi.org/v2/everything?q={query}&from=2025-01-16&sortBy=publishedAt&apiKey=dfa93611c63348f6b59c3c89312af6cd")
news= requests.get(url)
headlines = json.loads(news.text)
for article in headlines['articles']:
    print(article['title'])
    print(article['description'])
    print("-------------------------------")

