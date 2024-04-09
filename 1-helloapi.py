from tasks import get_task, get_token, send_answer


def hello_api():
    token = get_token("helloapi")
    task = get_task(token)

    cookie = task["cookie"]

    send_answer(token, cookie)


hello_api()
