import requests
from datetime import datetime

NUTRITION_APPLICATION_ID = "af45a6e4"
NUTRITION_API_KEY = "aa5a2e8ad889aee6fb83e0ad379d2cd5"

exercise_input = input("What exercise you did today? ")

headers = {
    "x-app-id": NUTRITION_APPLICATION_ID,
    "x-app-key": NUTRITION_API_KEY,
    "Content-Type": "application/json"
}

request_body = {
    "query": exercise_input,
}

NUTRITION_EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=NUTRITION_EXERCISE_ENDPOINT, headers=headers, json=request_body)
data = response.json()["exercises"][0]
exercise = data["name"].title()
duration = round(data["duration_min"])
calories = round(data["nf_calories"])

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")


SHEETY_POST_ENDPOINT = "https://api.sheety.co/1afd9c2ddcbd7c57bd2ac3668e7df932/workoutTracking/workouts"
SHEETY_GET_ENDPOINT = "https://api.sheety.co/1afd9c2ddcbd7c57bd2ac3668e7df932/workoutTracking/workouts"

sheety_params = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}
sheety_header = {
    "Authorization": "Bearer shivanshutheownerofthissheet"
}
sheety_response = requests.post(url=SHEETY_POST_ENDPOINT, json=sheety_params, headers=sheety_header)
print(sheety_response.text)




