import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv(".env")
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("OWM_API_KEY")
YOUR_PHONE_NUMBER = os.getenv("YOUR_PHONE_NUMBER")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
account_sid = os.getenv("TWILIO_ACC_ID")
auth_token = os.getenv("AUTH_TOKEN")

MY_LAT = Latitude_of_your_location
MY_LONG = Longitude_of_your_location

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_data_in_3_hour_period = weather_data["list"]

will_rain = False

for weather_conditions in weather_data_in_3_hour_period:
    if weather_conditions["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_=f'whatsapp:+{TWILIO_PHONE_NUMBER}',
        body="It's going to rain today. Remember to bring an umbrella!☔︎",
        to=f'whatsapp:+{YOUR_PHONE_NUMBER}'
    )
    print(message.status)
