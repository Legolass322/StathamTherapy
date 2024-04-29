import bcrypt
from datetime import datetime, timedelta
from jose import jwt

from config.config import config
from database.models.user import User


def hash_password(password: str):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed_password


def verify_password(hashed_password: str, input_password: str):
    return bcrypt.checkpw(input_password.encode("utf-8"), hashed_password)


def create_access_token(user: User) -> str:
    expires = datetime.now() + timedelta(minutes=config["auth"]["jwt_expiration"])

    to_encode = {"exp": expires, "user_id": user.id, "user_login": user.login}
    encoded_jwt = jwt.encode(
        to_encode, config["auth"]["jwt_secret"], config["auth"]["algorithm"]
    )
    return encoded_jwt


def create_refresh_token(user: User) -> str:
    expires = datetime.now() + timedelta(minutes=config["auth"]["rt_expiration"])

    to_encode = {"exp": expires, "user_id": user.id, "user_login": user.login}
    encoded_jwt = jwt.encode(
        to_encode, config["auth"]["rt_secret"], config["auth"]["algorithm"]
    )
    return encoded_jwt
