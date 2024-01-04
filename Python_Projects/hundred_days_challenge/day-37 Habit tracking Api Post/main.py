from datetime import datetime

import requests
import os
from dotenv import load_dotenv

pixela_endpoint = "https://pixe.la/v1/users"

load_dotenv()

USERNAME = "oskaras"
TODAY = datetime.now()

user_params = {
    "token": os.getenv("HABIT_TRACKER_TOKEN"),
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
#
# response = requests.post(url=pixela_endpoint, json=user_params)
#
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "kuro",
}
headers = {
    "X-USER-TOKEN": os.getenv("HABIT_TRACKER_TOKEN")
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response)

graph_data = {
    "date": f"{TODAY.strftime('%Y%m%d')}",
    "quantity": "5",
}

graph1_endpoint = f"{graph_endpoint}/graph1"

# response = requests.post(url=graph1_endpoint, json=graph_data, headers=headers)
# print(response)


graph_data_update = {
    "date": f"{TODAY.strftime('%Y%m%d')}",
    "quantity": "10.5",
}

graph1_endpoint_update = f"{graph_endpoint}/graph1/{TODAY.strftime('%Y%m%d')}"

# response = requests.put(url=graph1_endpoint_update, json=graph_data_update, headers=headers)
# print(response)


delete_endpoint = f"{graph_endpoint}/graph1/{TODAY.strftime('%Y%m%d')}"

# response = requests.delete(url=graph1_endpoint_update, headers=headers)
# print(response)


