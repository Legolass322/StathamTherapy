from fastapi import Body
from pydantic import BaseModel

from sqlite3 import IntegrityError

from app.providers.user import create_user
from .router import router

class SignupBody(BaseModel):
    login: str
    password: str

@router.post("/signup")
def signup(body: SignupBody = Body(...)):
    try:
        user = create_user(body["login"], body["password"])
    except IntegrityError:
        return 409, None

    return 200, user
