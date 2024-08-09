# Birthday Reminder & Email Sender

This project is a simple Python script that automatically sends personalized birthday emails to people listed in a CSV file. The script checks if today matches anyone's birthday and sends a pre-written email template with the person's name.

## Features

- Reads birthday data from a CSV file.
- Checks if today matches any birthdays, ignoring the year.
- Sends a personalized birthday email using random email templates.
- Uses SMTP to send emails via Gmail.

## Prerequisites

Before running the script, you need to have the following:

- Python 3.x installed on your system.
- A Gmail account to send emails.
- The required Python libraries:
  - `pandas`
  - `smtplib`
  - `datetime`