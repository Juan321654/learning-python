import requests
from datetime import datetime
import os

APP_ID = "81e93623"
API_KEY = "ad2bc55c2c227cf8b4aedde2de6e03e0"
post_excercise_endpoint = "https://api.sheety.co/4feb885d96e9c21c448e9158b335c0cf/myWorkouts/workouts"


GENDER = "male"
WEIGHT_KG = 100
HEIGHT_CM = 160
AGE = 31


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

print(os.environ.get('USER'))

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(post_excercise_endpoint, json=sheet_inputs)

    print(sheet_response.text)
