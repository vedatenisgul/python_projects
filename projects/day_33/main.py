import requests
import datetime as dt
import smtplib
import time

my_email = YOUR_EMAIL
my_password = YOUR_PASSWORD


MY_LAT = 41.003383
MY_LONG = 28.538565


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    longitude = float(response.json()['iss_position']['longitude'])
    latitude = float(response.json()['iss_position']['latitude'])

    if MY_LONG - 5 <= longitude <= MY_LONG + 5 and MY_LAT - 5 <= latitude <= MY_LAT + 5:
        return True
    else:
        return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    now = dt.datetime.now()
    current_hour = now.hour

    if current_hour > sunset or current_hour < sunrise:
        return True
    else:
        return False


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg=f"Subject:ISS is above you!\n\nLook Up!")
