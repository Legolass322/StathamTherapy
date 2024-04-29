from database.models.user import User
from database import database
from .utils import hash_password

def create_user(login: str, password: str):
    with database.Session() as session:
        new_user = User(login=login, passhash=hash_password(password))
        session.add(new_user)
        session.commit()
        return {"id": new_user.id, "login": new_user.login}
