import os

import requests
from dotenv import load_dotenv

load_dotenv()

WEBHOOK = os.getenv("MAKE_WEBHOOK_KNOWLEDGE")

response = requests.get(WEBHOOK)
print(response.json())
