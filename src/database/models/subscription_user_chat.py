import datetime
from sqlalchemy import Column, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship
from database.database import Base


class SubscriptionUserChat(Base):
    __tablename__ = "subscriptions_user_chat"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    chat_id = Column(Integer, ForeignKey("chats.id"), index=True)
    created_at = Column(DateTime, default=datetime.datetime.now())

    user = relationship("User", back_populates="user_subscriptions")
    chat = relationship("Chat", back_populates="chat_subscriptions")

    def __repr__(self) -> str:
        return f"SubscriptionUserChat(id={self.id!r}, user_id={self.user_id!r}, chat_id={self.chat_id!r}, created_at={self.created_at!r})"
