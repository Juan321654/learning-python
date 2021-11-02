import requests
from datetime import datetime

USERNAME = "juanca"
TOKEN = "jc2021python"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
  "token": TOKEN,
  "username": USERNAME,
  "agreeTermsOfService": "yes",
  "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
  "id": GRAPH_ID,
  "name": "Cycling Graph",
  "unit": "Km",
  "type": "float",
  "color": "ajisai"
}

headers = {
  "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# print(today.strftime("%Y%m%d")) # 20211101

pixel_data = {
  "date": today.strftime("%Y%m%d"),
  "quantity": input("How many kilometers did you cycle today? ")
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response)

# update_endpoint = f" "