from database.models.user import User
from database import database
from .utils import hash_password


def create_user(login: str, password: str):
    with database.db.session() as session:
        new_user = User(login=login, passhash=hash_password(password))
        session.add(new_user)
        session.commit()
        return new_user
