from database.models.subscription_user_chat import SubscriptionUserChat
from database.models.chat import Chat
from database import database


def get_user_chats(user_id: int, page_size: int, page_number: int):
    with database.db.session() as session:
        query = session.query(Chat)
        query = query.join(SubscriptionUserChat)
        query = query.filter(SubscriptionUserChat.user_id == user_id)
        query = query.order_by(SubscriptionUserChat.created_at)
        query = query.offset((page_number - 1) * page_size)
        query = query.limit(page_size)
        return query.all()
