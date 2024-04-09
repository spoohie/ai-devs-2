import json

import ai
import requests
import tasks

db_path = "resources/13-db.json"


def prepare_db():
    URL = "https://tasks.aidevs.pl/data/people.json"
    response = requests.get(URL)
    data = response.json()

    db = {}
    for d in data:
        name = d["imie"] + " " + d["nazwisko"]
        description = f"{d["o_mnie"]}, ulubiony kolor: {d["ulubiony_kolor"]}"
        db[name] = description
    with open(db_path, "w") as f:
        json.dump(db, f)


token = tasks.get_token("people")
task = tasks.get_task(token)
# prepare_db()

print(task["question"])
name = ai.chat(
    system="Przykłady:###\nQ: Jaki jest ulubiony kolor Krysi Ludek?\nA: Krystyna Ludek\nQ: Gdzie mieszka Szymon Rumcajs?\nA: Szymon Rumcajs\nQ: Jakie jest ulubione jedzenie Magdaleny Kot?\nA: Magdalena Kot###",
    content=f"Podaj imię i nazwisko osoby. Imię w mianowniku. Jeśli imię jest zdrobnione, podaj niezdrobnioną wersję: {task["question"]}",
    model="gpt-4",
)
print(name)

with open(db_path, encoding="utf-8") as f:
    db = json.load(f)
    answer = ai.chat(
        content=task["question"],
        system=f"Answer briefly in POLISH. Context: ```{name}: {db[name]}```",
    )
    tasks.send_answer(token, answer)
