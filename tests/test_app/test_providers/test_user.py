import pytest
from sqlalchemy import Table
from app.providers.user.create_user import create_user
from database import database

class TestUserProvider:
    @pytest.fixture
    def clear_users(self):
        users_table = Table("users", database.metadata)
        yield users_table
        with database.Session() as session:
            session.execute(users_table.delete())
            session.commit()

    def test_create_user(self, clear_users):
        user = create_user("test", "testhash")
        
        users_table = clear_users
        
        assert user["login"] == "test"
        with database.Session() as session:
            count = session.query(users_table).count()
            assert count == 1
