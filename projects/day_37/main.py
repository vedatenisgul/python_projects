import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables (e.g., your Pixela API token)
load_dotenv(".env")

# ** User Setup **

# Set your Pixela username
USERNAME = "vedat1"

# Retrieve your Pixela API token from environment variables
TOKEN = os.getenv("TOKEN")

# Pixela API endpoint for user management
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

# Parameters for creating a new Pixela user (if needed)
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# *******************************************************************
# Uncomment and run this block once to create a new Pixela user
# response = requests.post(url=PIXELA_ENDPOINT, json=user_parameters)
# print(response.text)
# ********************************************************************

# ** Graph Setup **

# Pixela API endpoint for managing graphs
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

# Unique identifier for your graph
GRAPH_ID = "graph1"
GRAPH_NAME = "Book Graph"
UNIT = "Page"
TYPE = "int"
COLOR = "ajisai"
# Parameters for creating a new graph
graph_parameters = {
    "id": GRAPH_ID,
    "name": GRAPH_NAME,
    "unit": UNIT,
    "type": TYPE,
    "color": COLOR,
}

# Headers for API requests that require authentication
headers = {
    "X-USER-TOKEN": TOKEN,
}

# *******************************************************************
# Uncomment and run this block once to create a new graph
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_parameters, headers=headers)
# print(response.text)
# ********************************************************************

# ** Adding and Updating Pixels (Data Points) **

# Pixela API endpoint for adding pixels to a graph
ADD_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

# Get today's date
today = datetime.now()

# Format the date as YYYYMMDD (required by Pixela)
DATE = today.strftime("%Y%m%d")

# Parameters for adding a new pixel
QUANTITY = "35"

adding_pixel_parameters = {
    "date": DATE,
    "quantity": QUANTITY,
}

# *******************************************************************
# Uncomment and run this block once to add a new pixel
# response = requests.post(url=ADD_PIXEL_ENDPOINT, json=adding_pixel_parameters, headers=headers)
# print(response.text)
# ********************************************************************

# Pixela API endpoint for updating a specific pixel
UPDATE_ENDPOINT = f"{ADD_PIXEL_ENDPOINT}/{DATE}"

# Parameters for updating a pixel
new_value = "7"
params = {
    "quantity": new_value,
}

# *******************************************************************
# Uncomment and run this block once to update a pixel
# response = requests.put(url=UPDATE_ENDPOINT, json=params, headers=headers)
# print(response.text)
# ********************************************************************

# ** Deleting a Pixel **

# Pixela API endpoint for deleting a specific pixel
date_you_want_to_delete = "20240715"
DELETE_ENDPOINT = f"{ADD_PIXEL_ENDPOINT}/{date_you_want_to_delete}"

# *******************************************************************
# Uncomment and run this block once to delete the pixel
# response = requests.delete(url=DELETE_ENDPOINT, headers=headers)
# print(response.text)
# ********************************************************************