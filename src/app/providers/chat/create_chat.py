from database.models.chat import Chat
from database import database


def create_chat():
    with database.db.session() as session:
        new_chat = Chat()
        session.add(new_chat)
        session.commit()
        return new_chat
