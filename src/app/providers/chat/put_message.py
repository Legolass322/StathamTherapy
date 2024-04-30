from database.models.message import Message
from database import database


def put_message(user_id: int, chat_id: int, text: str):
    with database.db.session() as session:
        message = Message(sender_id=user_id, chat_id=chat_id, text=text)
        session.add(message)
        session.commit()
        return message
