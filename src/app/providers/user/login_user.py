from database.models.user import User
from .utils import create_access_token, create_refresh_token


def login_user(user: User):
    return {
        "access_token": create_access_token(user),
        "refresh_token": create_refresh_token(user),
    }
