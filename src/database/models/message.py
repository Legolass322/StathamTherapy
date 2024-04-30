import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database.database import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("users.id"), index=True)
    chat_id = Column(Integer, ForeignKey("chats.id"), index=True)
    text = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now(), index=True)
    updated_at = Column(DateTime, default=datetime.datetime.now())

    sender = relationship("User", back_populates="messages")
    chat = relationship("Chat", back_populates="messages")

    def __repr__(self) -> str:
        return f"Message(id={self.id!r}, sender_id={self.sender_id!r}, chat_id={self.chat_id!r}, created_at={self.created_at!r}, updated_at={self.updated_at!r})"

    def to_json(self):
        return {
            "id": int(self.id),
            "sender_id": int(self.sender_id),
            "chatid": int(self.chat_id),
            "text": self.text,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }
