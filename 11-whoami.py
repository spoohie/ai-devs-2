import time

import ai
import tasks

base_knowledge = set()

messages = [
    {
        "role": "system",
        "content": "Try to guess who is this about. Return only his/hers name and surname. If you don't know or you're not absolutely certain, return NIE.",
    },
]

while True:
    token = tasks.get_token("whoami")
    task = tasks.get_task(token)

    if not task:
        print("Request limit. Sleeping...")
        time.sleep(10)
        continue
    hint = task["hint"]
    if hint in base_knowledge:
        continue
    base_knowledge.add(hint)
    messages.append({"role": "user", "content": f"hint: {hint}. Who is the person?"})
    answer = ai.conversation(messages)
    print(answer)

    if answer == "NIE":
        continue
    evaluation = tasks.send_answer(token, answer)

    if evaluation["code"] == 0:
        break


# text = None
# while True:
#     response = requests.get(task["input"], headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"})
#     if response.status_code == 200:
#         text = response.text
#         break
#     print(f"Received {response.status_code}, retrying in 2 seconds")
#     time.sleep(2)

# answer = ai.chat(content=task["question"], system="Answer briefly in POLISH. Context: ```" + text + "```")

# tasks.send_answer(token, answer)
