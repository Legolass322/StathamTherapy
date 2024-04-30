import pytest
from sqlalchemy import Table

from app.providers.chat.create_new_dialogue import create_new_dialogue
from app.providers.chat.get_chat_messages import get_chat_messages
from app.providers.chat.get_user_chats import get_user_chats
from app.providers.chat.put_message import put_message
from app.providers.user.create_user import create_user
from database import database
from database.models.user import User


class TestUserProvider:
    @pytest.fixture
    def users(self):
        users = Table("users", database.metadata)
        yield (
            create_user("userA", "pass"),
            create_user("userB", "pass"),
            create_user("userC", "pass"),
        )
        with database.db.session() as session:
            session.execute(users.delete())
            session.commit()

    @pytest.fixture
    def tables(self):
        chats_table = Table("chats", database.metadata)
        subscriptions_table = Table("subscriptions_user_chat", database.metadata)
        messages = Table("messages", database.metadata)
        yield (chats_table, subscriptions_table, messages)
        with database.db.session() as session:
            session.execute(chats_table.delete())
            session.execute(subscriptions_table.delete())
            session.execute(messages.delete())
            session.commit()

    def test_chatting(self, tables: tuple[Table, Table, Table], users: tuple[User, User, User]):
        chats, subscriptios, messages = tables
        userA, userB, userC = users
        
        with database.db.session() as session:
            assert session.query(chats).count() == 0
            assert session.query(subscriptios).count() == 0
            assert session.query(messages).count() == 0
            
            chatAB = create_new_dialogue(userA.id, userB.id)
            
            assert session.query(chats).count() == 1
            assert session.query(subscriptios).count() == 2

            chatAC = create_new_dialogue(userA.id, userC.id)
            
            assert session.query(chats).count() == 2
            assert session.query(subscriptios).count() == 4
            
            chatBC = create_new_dialogue(userB.id, userC.id)
            
            assert session.query(chats).count() == 3
            assert session.query(subscriptios).count() == 6
            
            chatsOfA = get_user_chats(userA.id, 10, 1)
            
            assert len(chatsOfA) == 2
            
            messageAtoB = put_message(userA.id, chatAB.id, "messageAtoB")
            messageAtoC = put_message(userA.id, chatAC.id, "messageAtoC")
            messageBtoC = put_message(userB.id, chatBC.id, "messageBtoC")
            messageBtoA = put_message(userB.id, chatAB.id, "messageBtoA")
            
            messagesOfAB = get_chat_messages(chatAB.id, 10, 1)
            messagesOfAC = get_chat_messages(chatAC.id, 10, 1)
            messagesOfBC = get_chat_messages(chatAC.id, 10, 1)
            
            assert len(messagesOfAB) == 2
            assert len(messagesOfAC) == 1
            assert len(messagesOfBC) == 1
            
            
