from database.models.subscription_user_chat import SubscriptionUserChat
from database.models.chat import Chat
from database import database


def subscribe_chat(user_id: int, chat_id: int):
    with database.db.session() as session:
        subscription = SubscriptionUserChat(user_id=user_id, chat_id=chat_id)
        session.add(subscription)
        session.commit()
