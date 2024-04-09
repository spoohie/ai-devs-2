import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

BASE_URL = "https://tasks.aidevs.pl"
TOKEN_URL = BASE_URL + "/token/{task}"
TASK_URL = BASE_URL + "/task/{token}"
ANSWER_URL = BASE_URL + "/answer/{token}"


def get_token(task: str):
    APIKEY_PAYLOAD = json.dumps({"apikey": API_KEY})
    response = requests.request(
        "POST", TOKEN_URL.format(task=task), headers={}, data=APIKEY_PAYLOAD
    )
    return response.json()["token"]


def get_task(token: str):
    response = requests.request("GET", TASK_URL.format(token=token), headers={})
    if response.status_code != 200:
        print(response.text)
        return None
    return response.json()


def post_task(token: str, payload: str):
    response = requests.request("POST", TASK_URL.format(token=token), headers={}, data=payload)
    return response.json()


def send_answer(token: str, answer):
    response = requests.request(
        "POST",
        ANSWER_URL.format(token=token),
        headers={},
        data=json.dumps({"answer": answer}),
    )
    print(response.json())
    return response.json()
