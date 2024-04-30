import datetime
from sqlalchemy import Column, Integer, String, DateTime
from database.database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True)
    passhash = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now())

    user_subscriptions = relationship("SubscriptionUserChat", back_populates="user")
    messages = relationship("Message", back_populates="sender")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, login={self.login!r}, created_at={self.created_at!r})"
