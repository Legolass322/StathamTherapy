import pytest
from sqlalchemy import Table
from fastapi.testclient import TestClient
from app.providers.chat.create_new_dialogue import create_new_dialogue
from app.providers.user.create_user import create_user
from database import database
from app.main import app
from database.models.chat import Chat
from database.models.user import User


client = TestClient(app)

raw_users = [
    {"login": "userA", "password": "pass"},
    {"login": "userB", "password": "pass"},
]


class TestChat:
    @pytest.fixture
    def users(self):
        userA = create_user(**raw_users[0])
        userB = create_user(**raw_users[1])
        users_table = Table("users", database.metadata)
        yield (userA, userB)
        with database.db.session() as session:
            session.execute(users_table.delete())
            session.commit()

    @pytest.fixture
    def tables(self):
        chats_table = Table("chats", database.metadata)
        subscriptions_table = Table("subscriptions_user_chat", database.metadata)
        messages_table = Table("messages", database.metadata)
        yield (chats_table, subscriptions_table, messages_table)
        with database.db.session() as session:
            session.execute(chats_table.delete())
            session.execute(subscriptions_table.delete())
            session.execute(messages_table.delete())
            session.commit()

    @pytest.fixture
    def dialogue(self, users: tuple[User, User], tables: tuple[Table, Table, Table]):
        userA, userB = users
        chatAB = create_new_dialogue(userA.id, userB.id)
        yield chatAB

    @pytest.fixture
    def tokens(self, users: tuple[User, User]):
        responseA = client.post(
            "/api/auth/login",
            json={
                "username": raw_users[0]["login"],
                "password": raw_users[0]["password"],
            },
        )

        assert responseA.status_code == 200

        access_token_a = responseA.json()["access_token"]

        responseB = client.post(
            "/api/auth/login",
            json={
                "username": raw_users[1]["login"],
                "password": raw_users[1]["password"],
            },
        )

        assert responseB.status_code == 200

        access_token_b = responseB.json()["access_token"]

        yield (access_token_a, access_token_b)

    def test_send_message(self, dialogue: Chat, tables, users, tokens: tuple[str, str]):
        chatAB = dialogue
        chats, subscriptions, messages = tables

        responseA1 = client.post(
            "/api/chat/send_message",
            json={"chat_id": chatAB.id, "text": "a1"},
            headers={"Authorization": f"Bearer {tokens[0]}"},
        )

        assert responseA1.status_code == 200

        responseB1 = client.post(
            "/api/chat/send_message",
            json={"chat_id": chatAB.id, "text": "b1"},
            headers={"Authorization": f"Bearer {tokens[1]}"},
        )

        assert responseB1.status_code == 200

        with database.db.session() as session:
            assert session.query(messages).count() == 2

    def test_messages(self, dialogue: Chat, tables, users, tokens: tuple[str, str]):
        chatAB = dialogue
        chats, subscriptions, messages = tables

        for i in range(8):
            res = client.post(
                "/api/chat/send_message",
                json={"chat_id": chatAB.id, "text": f"a{i}"},
                headers={"Authorization": f"Bearer {tokens[0]}"},
            )

            assert res.status_code == 200

        for i in range(8):
            res = client.post(
                "/api/chat/send_message",
                json={"chat_id": chatAB.id, "text": f"b{i}"},
                headers={"Authorization": f"Bearer {tokens[1]}"},
            )

            assert res.status_code == 200

        with database.db.session() as session:
            assert session.query(messages).count() == 16
            
        response1 = client.get(
            "/api/chat/messages",
            params={"page_number": 1, "page_size": 10, "chat_id": chatAB.id},
            headers={"Authorization": f"Bearer {tokens[0]}"},
        )

        assert response1.status_code == 200
        assert len(response1.json()) == 10
        
        response2 = client.get(
            "/api/chat/messages",
            params={"page_number": 2, "page_size": 10, "chat_id": chatAB.id},
            headers={"Authorization": f"Bearer {tokens[0]}"},
        )
        
        assert response2.status_code == 200
        assert len(response2.json()) == 6
