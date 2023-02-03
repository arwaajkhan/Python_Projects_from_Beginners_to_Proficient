import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 62
HEIGHT_CM = 178
AGE = 25

APP_ID = "5c830e1c"
API_KEY = "YOUR_KEY"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/78931bd35731db468b90fb1feb4e199d/myWorkouts/workouts"

exercise_text = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
today_time = datetime.now().strftime("%X")

headers = {

}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        url=sheety_endpoint,
        json=sheet_inputs,
        auth=(
            "YOUR_USERNAME",
            "YOUR_PASSWORD"
        ))
    print(sheet_response.text)
