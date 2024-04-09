import tasks

token = tasks.get_token("functions")

add_user_schema = {
    "name": "addUser",
    "description": "Add a user with name, surname and year",
    "parameters": {
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
                "description": "User's name",
            },
            "surname": {
                "type": "string",
                "description": "User's surname",
            },
            "year": {
                "type": "integer",
                "description": "User's year",
            },
        },
        "required": ["name", "surname", "year"],
    },
}

tasks.send_answer(token, add_user_schema)
