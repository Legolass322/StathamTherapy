import datetime
from sqlalchemy import Column, Integer, DateTime
from database.database import Base


class Chat(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True, index=True)
    user1_id = Column(Integer, index=True)
    user2_id = Column(Integer, index=True)
    created_at = Column(DateTime, default=datetime.datetime.now(), index=True)
    updated_at = Column(DateTime, default=datetime.datetime.now())

    def __repr__(self) -> str:
        return f"Chat(id={self.id!r}, user1_id={self.user1_id!r}, user2_id={self.user2_id!r}, created_at={self.created_at!r}, updated_at={self.updated_at!r})"
