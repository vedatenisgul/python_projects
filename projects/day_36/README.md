**Stock News Notifier**

This Python script monitors stock prices and sends news alerts via WhatsApp if there's a significant change (5% or more) over two days.

**Requirements:**

* Python 3.x
* `requests` library (`pip install requests`)
* `dotenv` library (`pip install python-dotenv`)
* `twilio` library (`pip install twilio`)
* A Twilio account with WhatsApp Business enabled ([https://www.twilio.com/en-us/client/mobile](https://www.twilio.com/en-us/client/mobile))
* An Alpha Vantage API key ([https://www.alphavantage.co/premium/](https://www.alphavantage.co/premium/))
* A News API key ([[https://newsapi.org/](https://newsapi.org/)])

**Setup:**
* You should fill the **env.txt** file and convert it's name to **.env**.