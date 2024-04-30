from database import database
from database.models.subscription_user_chat import SubscriptionUserChat
from database.models.user import User


def check_user_has_chat(user_id: int, chat_id: int):
    with database.db.session() as session:
        query = session.query(SubscriptionUserChat).filter(User.id == user_id)
        query = query.filter(SubscriptionUserChat.chat_id == chat_id)
        
        return query.first() is not None