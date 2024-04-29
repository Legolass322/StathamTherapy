import datetime
from sqlalchemy import Column, Integer, String, DateTime
from database.database import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(Integer, index=True)
    text = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now(), index=True)
    updated_at = Column(DateTime, default=datetime.datetime.now())

    def __repr__(self) -> str:
        return f"Message(id={self.id!r}, chat_id={self.chat_id!r}, created_at={self.created_at!r}, updated_at={self.updated_at!r})"
