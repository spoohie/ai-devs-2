import time

import ai
import requests
import tasks

token = tasks.get_token("scraper")
task = tasks.get_task(token)

text = None
while True:
    response = requests.get(
        task["input"],
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        },
    )
    if response.status_code == 200:
        text = response.text
        break
    print(f"Received {response.status_code}, retrying in 2 seconds")
    time.sleep(2)

answer = ai.chat(
    content=task["question"], system="Answer briefly in POLISH. Context: ```" + text + "```"
)

tasks.send_answer(token, answer)
