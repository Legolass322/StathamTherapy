import datetime
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import relationship
from database.database import Base


class Chat(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.now(), index=True)
    updated_at = Column(DateTime, default=datetime.datetime.now())

    chat_subscriptions = relationship("SubscriptionUserChat", back_populates="chat")
    messages = relationship("Message", back_populates="chat")

    def __repr__(self) -> str:
        id = self.id
        created_at = self.created_at
        updated_at = self.updated_at
        return f"Chat(id={id!r}, created_at={created_at!r}, updated_at={updated_at!r})"
