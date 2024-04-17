import os

import tasks
from dotenv import load_dotenv

load_dotenv()

WEBHOOK = os.getenv("MAKE_WEBHOOK_GOOGLE")

token = tasks.get_token("google")
task = tasks.get_task(token)

tasks.send_answer(token, WEBHOOK)
