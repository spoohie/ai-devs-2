import ai
import requests
import tasks
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams

COLLECTION = "AI_DEVS"


def populate_qdrant(client: QdrantClient):
    qdrant_client.recreate_collection(
        collection_name=COLLECTION,
        vectors_config=VectorParams(size=1536, distance=Distance.COSINE),
    )

    URL = "https://unknow.news/archiwum_aidevs.json"

    response = requests.get(URL)
    data = response.json()

    points = []
    for idx, d in enumerate(data):
        description = d["title"] + " " + d["info"]
        embedding = ai.get_embedding(description)
        points.append(PointStruct(id=idx, vector=embedding, payload={"url": d["url"]}))

    qdrant_client.upsert(collection_name=COLLECTION, points=points)


qdrant_client = QdrantClient(url="localhost:6333")
# populate_qdrant(qdrant_client)

token = tasks.get_token("search")
task = tasks.get_task(token)

query_embedding = ai.get_embedding(task["question"])
answer = qdrant_client.search(collection_name=COLLECTION, query_vector=query_embedding, limit=1)[0]

tasks.send_answer(token, answer.payload["url"])
