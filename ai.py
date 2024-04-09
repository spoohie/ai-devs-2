from openai import OpenAI
from tasks import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def chat(content: str, system: str = None, model="gpt-3.5-turbo"):
    messages = [
        {
            "role": "user",
            "content": content,
        }
    ]
    if system:
        messages.append({"role": "system", "content": system})
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model,
    )
    return chat_completion.choices[0].message.content


def conversation(messages: list):
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content


def get_embedding(text: str, model="text-embedding-ada-002", **kwargs) -> list[float]:
    text = text.replace("\n", " ")
    return client.embeddings.create(input=text, model=model).data[0].embedding
