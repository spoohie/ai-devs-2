import tasks
from ai import client

token = tasks.get_token("embedding")
phrase = "Hawaiian pizza"

embedding = client.embeddings.create(input=phrase, model="text-embedding-ada-002").data[0].embedding

tasks.send_answer(token, embedding)
