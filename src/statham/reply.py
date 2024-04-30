import random

from .collection import collection


def get_reply(message: str):
    if message == "ping":
        return "Pong! Type of Statham today - Random"

    random_choice = random.choice(collection)

    return random_choice
