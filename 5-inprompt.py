import ai
import tasks

token = tasks.get_token("inprompt")
task = tasks.get_task(token)

question = task["question"]
data_input = task["input"]

name = ai.chat(
    content=f'Pytanie brzmi: "{question}" Podaj imie osoby z pytania', system="Zwróć TYLKO imię"
)

context = ". ".join([d for d in data_input if name in d])

answer = ai.chat(content=question, system=f"Context: ```{context}```")
tasks.send_answer(token, answer)
