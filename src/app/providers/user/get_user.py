from database.models.user import User
from database import database


def get_user_by_id(id: str):
    with database.db.session() as session:
        return session.query(User).filter(User.id == id).first()


def get_user_by_login(login: str):
    with database.db.session() as session:
        return session.query(User).filter(User.login == login).first()
