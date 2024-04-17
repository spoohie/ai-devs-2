import os

import tasks
from dotenv import load_dotenv

load_dotenv()

WEBHOOK = os.getenv("MAKE_WEBHOOK_OWNAPIPRO")

token = tasks.get_token("ownapipro")
task = tasks.get_task(token)

tasks.send_answer(token, WEBHOOK)

