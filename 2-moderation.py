import tasks
from openai import OpenAI

client = OpenAI(api_key=tasks.OPENAI_API_KEY)

token = tasks.get_token("moderation")
task = tasks.get_task(token)

input_to_moderate = task["input"]
answer = []

for i in input_to_moderate:
    response = client.moderations.create(input=i)
    answer.append(1 if response.results[0].flagged else 0)

tasks.send_answer(token, answer)
