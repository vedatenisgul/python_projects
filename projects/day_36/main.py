import os
import requests
import datetime as dt
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv(".env")
YOUR_PHONE_NUMBER = os.getenv("YOUR_PHONE_NUMBER")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
account_sid = os.getenv("TWILIO_ACC_ID")
auth_token = os.getenv("AUTH_TOKEN")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
STOCK_API_KEY = os.getenv("STOCK_API_KEY")


one_day = dt.timedelta(days=1)
two_day = dt.timedelta(days=2)
yesterday = str(dt.date.today() - one_day)
day_before_yesterday = str(dt.date.today() - two_day)


parameters_for_news = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME,
    "from": day_before_yesterday,
    "to": yesterday
}

parameters_for_stocks = {
    "apikey": STOCK_API_KEY,
    "symbol": STOCK,
    "outputsize": "compact",
    "function": "TIME_SERIES_DAILY",
}
response_1 = requests.get(STOCK_ENDPOINT, params=parameters_for_stocks)
response_1.raise_for_status()

yesterday_closing_price = response_1.json()["Time Series (Daily)"][yesterday]["4. close"]
day_before_yesterday_closing_price = response_1.json()["Time Series (Daily)"][day_before_yesterday]["4. close"]


amount_of_change = ((float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
                    / float(day_before_yesterday_closing_price))

if abs(amount_of_change) >= 0.05:
    response = requests.get(NEWS_ENDPOINT, params=parameters_for_news)
    response.raise_for_status()
    three_articles = response.json()["articles"][:3]
    client = Client(account_sid, auth_token)

    if amount_of_change > 0:
        amount_of_change = "⬆" + str(round(amount_of_change * 100))
    elif amount_of_change < 0:
        amount_of_change = "⬇" + str(round(amount_of_change * 100))

    [client.messages.create(
        from_=f'whatsapp:+{TWILIO_PHONE_NUMBER}',
        body=f"{STOCK}: {amount_of_change}%\nHeadline: {article['title']}\nBrief: {article['description']}",
        to=f'whatsapp:+{YOUR_PHONE_NUMBER}'

    ) for article in three_articles]


