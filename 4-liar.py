import ai
import tasks

token = tasks.get_token("liar")
question = "What is the capital of France?"
response = tasks.post_task(token, {"question": question})
answer_to_question = response["answer"]

answer = ai.chat(
    content=f'Question was: "{question}" Is this the answer? "{answer_to_question}"',
    system="Respond ONLY YES/NO",
)
tasks.send_answer(token, answer)
