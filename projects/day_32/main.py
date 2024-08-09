import datetime as dt
import random
import smtplib
import pandas

my_email = YOUR_EMAİL
my_password = YOUR_PASSWORD

birthday_data = pandas.read_csv("birthdays.csv")

people_list = []

for index, row in birthday_data.iterrows():
    person_dict = {
        "name": row['name'],
        "email": row['email'],
        "birth_date": (int(row['month']), int(row['day']))
    }
    people_list.append(person_dict)

now = dt.datetime.now()
current_date = (now.month, now.day)
letters_paths = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

for person in people_list:
    if current_date == person["birth_date"]:
        to_email = person["email"]
        with open(random.choice(letters_paths)) as file:
            file_text = file.read().replace("[NAME]", person['name'])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=to_email,
                                msg=f"Subject:Happy Birthday!\n\n{file_text}")






