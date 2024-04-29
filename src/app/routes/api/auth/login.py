from typing import Annotated
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from app.providers.user.login_user import login_user
from fastapi import Depends, HTTPException, status

from app.providers.user.get_user import get_user_by_login
from app.providers.user.utils import verify_password
from app.schemas.auth import IncorrectCredentials, SignBody, SuccessAuthTokens
from .router import router


async def _login(username: str, password: str):
    user = get_user_by_login(username)

    if user is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "No such user")

    if not verify_password(user.passhash, password):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Incorrect password")

    tokens = login_user(user)

    return JSONResponse(tokens)


@router.post(
    "/login",
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": IncorrectCredentials},
        status.HTTP_404_NOT_FOUND: {"model": IncorrectCredentials},
        status.HTTP_200_OK: {"model": SuccessAuthTokens},
    },
)
async def login_body(body: SignBody):
    return await _login(body.username, body.password)


@router.post(
    "/login_form",
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": IncorrectCredentials},
        status.HTTP_404_NOT_FOUND: {"model": IncorrectCredentials},
        status.HTTP_200_OK: {"model": SuccessAuthTokens},
    },
)
async def login_form(form: Annotated[OAuth2PasswordRequestForm, Depends()]):
    return await _login(form.username, form.password)
