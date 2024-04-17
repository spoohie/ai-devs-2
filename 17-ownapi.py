import os

import tasks
from dotenv import load_dotenv

load_dotenv()

WEBHOOK = os.getenv("MAKE_WEBHOOK_OWNAPI")

token = tasks.get_token("ownapi")
task = tasks.get_task(token)

tasks.send_answer(token, WEBHOOK)
