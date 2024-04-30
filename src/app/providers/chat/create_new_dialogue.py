from database import database
from database.models.chat import Chat
from database.models.subscription_user_chat import SubscriptionUserChat


def create_new_dialogue(userA_id: int, userB_id: int):
    with database.db.session() as session:
        chat = Chat()
        session.add(chat)
        session.commit()
        subscribeA = SubscriptionUserChat(user_id=userA_id, chat_id=chat.id)
        subscribeB = SubscriptionUserChat(user_id=userB_id, chat_id=chat.id)
        session.add(subscribeA)
        session.add(subscribeB)
        session.commit()
        return chat
