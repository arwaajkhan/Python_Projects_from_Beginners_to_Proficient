import requests
from datetime import datetime

USERNAME = "YOUR_USERNAME"
TOKEN = "YOUR_TOKEN"
GRAPH_ID = "graph1"

# [1] Create your user account

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}


# [2] Create a graph definition
# [3] Get the graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}


# [4] Post value to the graph


graph_creation = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2022, month=12, day=16)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "15"  # alternative: input("How many km did you cycle today?")
}


# [5] update graph using PUT

put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20221216"

pixel_up_data = {
    "quantity": "5"
}


# [6] delete the graph item using DELETE

del_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=del_endpoint, headers=headers)
print(response.text)
