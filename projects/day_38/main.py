import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv(".env")
API_KEY = os.getenv("API_KEY")
APP_ID = os.getenv("APP_ID")

API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

GENDER = "male"
WEIGHT_KG = "80"
HEIGHT_CM = "180"
AGE = 18

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

params = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}


response = requests.post(url=API_ENDPOINT, headers=headers, json=params)
response.raise_for_status()

SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")

now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%X")


USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
AUTH = os.getenv("AUTHORIZATION")
authorization_header = {
    "Authorization": AUTH,
}

for exercise in response.json()["exercises"]:
    exercise_data = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    sheet_response = requests.post(url=SHEETY_ENDPOINT, json=exercise_data, auth=(USERNAME, PASSWORD)
                                   , headers=authorization_header)
    sheet_response.raise_for_status()