from app.providers.user.create_user import create_user
from app.providers.user.get_user import get_user_by_login
from logger.logger import logger
from app.providers.chat.put_message import put_message
from statham.reply import get_reply


class StathamUser:
    def __init__(self):
        self.user_id = None

    def init(self):
        user = get_user_by_login("Statham")
        if user is None:
            user = create_user("Statham", "AlphaSigma")  # Wolves do not hide, they seek
        self.user_id = user.id

    def reply(self, chat_id: int, message: str):
        if self.user_id is None:
            logger.warn("Statham is not defined")
            return
        put_message(self.user_id, chat_id, get_reply(message))


statham_user = StathamUser()
