from fastapi import Body
from pydantic import BaseModel

from sqlite3 import IntegrityError

from app.providers.user import create_user

class SignupBody(BaseModel):
    login: str
    password: str

def signup(body: SignupBody = Body(...)):
    try:
        user = create_user(body["login"], body["password"])
    except IntegrityError:
        return 422, None

    return 200, user
