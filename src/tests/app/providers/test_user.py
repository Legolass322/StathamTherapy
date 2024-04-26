import pytest
from sqlalchemy import Table
from sqlalchemy.orm import Session
from app.providers.user.create_user import create_user
from database import database
from tests.fixtures.db_engine import engine

class TestUserProvider:
    @pytest.fixture
    def engine(self, monkeypatch: pytest.MonkeyPatch):
        monkeypatch.setattr(database, 'engine', engine)
        return engine

    @pytest.fixture
    def clear_users(self, engine):
        users_table = Table("users", database.metadata)
        yield users_table
        with Session(engine) as session:
            session.execute(users_table.delete())
            session.commit()

    def test_create_user(self, engine, clear_users: Table):
        user = create_user("test", "testhash")
        
        users_table = clear_users
        
        assert user["login"] == "test"
        with Session(engine) as session:
            count = session.query(users_table).count()
            assert count == 1
