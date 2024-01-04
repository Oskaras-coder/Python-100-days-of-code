import requests

from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

GENDER = "Male"
WEIGHT_KG = 82
HEIGHT_CM = 196
AGE = 24

headers = {
    "x-app-id": os.getenv("NUTRITION_X_API_ID"),
    "x-app-key": os.getenv("NUTRITION_X_API_KEY"),
}


exercise_text = input("Tell me which exercises you did: ")
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
sheety_post_endpoint = os.getenv("SHEET_ENDPOINT")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(sheety_post_endpoint,
                                   json=sheet_inputs,
                                   auth=(os.getenv("NUTRITION_X_API_AUTH_USERNAME"),
                                         os.getenv("NUTRITION_X_API_AUTH_PASSWORD")))

    print(sheet_response.text)

