from bs4 import BeautifulSoup
from article import Article
import pandas as pd
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

spans = soup.find_all(class_="titleline")
scores = soup.find_all(class_="score")
articles = []

for span, score in zip(spans, scores):
    anchor = span.find(name="a")
    article_name = anchor.getText()
    article_link = anchor.get("href")
    print(article_link)
    article_upvote = score.getText()

    articles.append(Article(article_name, article_link, article_upvote))

sorted_articles = sorted(articles, key=lambda article_obj: article_obj.upvote)[::-1]

data = [vars(article) for article in sorted_articles]
df = pd.DataFrame(data)
df.to_csv("article_list.csv")



