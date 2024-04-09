import requests
import tasks
from ai import client
from urlextract import URLExtract

path = "resources/7-mateusz.mp3"
token = tasks.get_token("whisper")
task = tasks.get_task(token)

extractor = URLExtract()
url = extractor.find_urls(task["msg"])[0]

response = requests.get(url)
if response.status_code == 200:
    with open(path, "wb") as f:
        f.write(response.content)

transcript = client.audio.transcriptions.create(
    file=open(path, "rb"),
    model="whisper-1",
    prompt="",
).text

tasks.send_answer(token, transcript)
