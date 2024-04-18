import ai
import tasks

token = tasks.get_token("md2html")
task = tasks.get_task(token)

response = ai.chat(system="md2html", content=f"{task['msg']}: {task['input']}", model="ft:gpt-3.5-turbo-0125:personal:aidevs:9FKfulVg")

tasks.send_answer(token, response)
