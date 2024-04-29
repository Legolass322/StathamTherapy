from sqlalchemy.orm import Session

from database.models.user import User
from database import database

def create_user(login: str, password: str):
    with Session(database.engine) as session:
        new_user = User(login=login, passhash=password, salt="some salt todo")
        session.add(new_user)
        session.commit()
        return {"id": new_user.id, "login": new_user.login}
