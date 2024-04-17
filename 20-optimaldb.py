import json
from collections import defaultdict

import ai
import tasks

json_path = "resources/3friends.json"
json_path_optimised = "resources/3friends_optimised.json"


def chunker(seq, size):
    return (seq[pos : pos + size] for pos in range(0, len(seq), size))


def prepare_db():
    with open(json_path) as f:
        data = json.load(f)

        # print(data)
        optimised_json = defaultdict(list)
        for name, sentences in data.items():
            for sentence in chunker(sentences, 10):
                optimised = optimise_sentences(name, sentence)
                print(optimised)
                optimised_json[name].append(optimised)

        with open("resources/3friends_optimised.json", "w") as f:
            json.dump(optimised_json, f)


def optimise_sentences(name, sentences):
    return ai.chat(
        content=f"Skróć i uprość podane zdania do minimum 5 slow kazde. Nie utrać znaczenia ani treści zadnego z nich. Zwróć ich tyle samo. Nie podawaj imienia. Nie numeruj zdań. Zwróć kazde zdanie w nowej linii. Zwróć tylko zdania, nic więcej. Przykłady```Before: Podczas ostatniej konferencji technologicznej, program który stworzył Zygfryd wygrał nagrodę za innowacyjność w użyciu JavaScript. After: Program, konferencja technologiczna, innowacyjność, JavaScript. Before: Wielu nie wie, ale ulubionym instrumentem muzycznym Anny jest ukulele, na którym gra po nocach, kiedy kodowanie na dziś się skończy. After: Instrument muzyczny, ukulele, noc, kodowanie. Before: Zygfryd: Jest znany z tego, że zawsze nosi ze sobą swojego laptopa, na którym zawsze ma otwarte kilka okien przeglądarki. After: Laptop, otwarte okna przeglądarki.``` Zdania: {sentences}",
        model="gpt-4",
    )


def stringify_db(db):
    return "\n".join([f"{name}: {' '.join(sentences)}" for name, sentences in db.items()])


token = tasks.get_token("optimaldb")
task = tasks.get_task(token)

# prepare_db()

with open(json_path_optimised, encoding="utf-8") as f:
    db = json.load(f)
    tasks.send_answer(token, stringify_db(db))
