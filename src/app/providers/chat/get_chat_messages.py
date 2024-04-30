from database.models.message import Message
from database.models.chat import Chat
from database import database


def get_chat_messages(chat_id: int, page_size: int, page_number: int):
    with database.db.session() as session:
        query = session.query(Message)
        query = query.filter(Message.chat_id == chat_id)
        query = query.order_by(Message.created_at.desc())
        query = query.offset((page_number - 1) * page_size)
        query = query.limit(page_size)
        return query.all()
