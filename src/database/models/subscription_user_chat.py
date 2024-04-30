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
        fields = {
            "id": self.id,
            "user_id": self.user_id,
            "chat_id": self.chat_id,
            "created_at": self.created_at,
        }
        formatted = [f"{k}: {v}" for k, v in fields]
        string = ", ".join(formatted)
        return f"SubscriptionUserChat({string})"
