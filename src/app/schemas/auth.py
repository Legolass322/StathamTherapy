from pydantic import BaseModel, Field

from app.schemas.common import Message


class SignBody(BaseModel):
    username: str = Field(..., strip_whitespace=True, min_length=4)
    password: str = Field(..., min_length=4)


class IncorrectCredentials(Message):
    pass


class AuthTokenData(BaseModel):
    exp: int
    user_id: int
    user_login: str


class SuccessAuthTokens(BaseModel):
    access_token: str
    refresh_token: str
