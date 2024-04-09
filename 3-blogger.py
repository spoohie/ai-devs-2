import json

import ai
import tasks

token = tasks.get_token("blogger")
task = tasks.get_task(token)

answer = ai.chat(
    content=f"Give me a blog post with 4 sentences for every chapter.: {task["blog"]}",
    system="Respond as JSON list",
)
tasks.send_answer(token, json.loads(answer))
