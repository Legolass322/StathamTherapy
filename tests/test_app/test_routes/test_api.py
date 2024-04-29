import pytest
from sqlalchemy import Table
from contextlib import nullcontext as does_not_raise

from app.providers.user.create_user import create_user
from app.schemas.auth import SuccessAuthTokens
from database import database

from fastapi.testclient import TestClient

from app.main import app
from database.models.user import User

client = TestClient(app)


class TestAuth:
    @pytest.fixture
    def users_table(self):
        create_user("user", "password")
        users_table = Table("users", database.metadata)
        yield users_table
        with database.db.session() as session:
            session.execute(users_table.delete())
            session.commit()

    @pytest.mark.parametrize(
        "login,password,status_code",
        [
            ("userA", "password", 200),
            ("user", "password", 409),
            ("u", "password", 422),
            ("some", "p", 422),
        ],
    )
    def test_signup(self, users_table, login, password, status_code):
        response = client.post(
            "/api/auth/signup", json={"username": login, "password": password}
        )

        assert response.status_code == status_code

        if response.status_code == 200:
            with does_not_raise():
                SuccessAuthTokens(**response.json())

    @pytest.mark.parametrize(
        "login,password,status_code",
        [
            ("userA", "password", 404),
            ("user", "password", 200),
            ("user", "another-password", 401),
            ("user", "p", 422),
        ],
    )
    def test_login(self, users_table, login, password, status_code):
        response = client.post(
            "/api/auth/login", json={"username": login, "password": password}
        )

        assert response.status_code == status_code

        if response.status_code == 200:
            with does_not_raise():
                SuccessAuthTokens(**response.json())
    
    def test_auth_me(self, users_table):
        login_response = client.post(
            "/api/auth/login", json={"username": "user", "password": "password"}
        )
        
        assert login_response.status_code == 200
        
        access_token = login_response.json()["access_token"]
        
        response = client.get(
            "/api/auth/me", headers={
                "Authorization": f"Bearer {access_token}"
            }
        )
        
        assert response.status_code == 200
        
        with does_not_raise():
            User(**response.json())