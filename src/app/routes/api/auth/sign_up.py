from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from app.providers.user.login_user import login_user
from app.providers.user.create_user import create_user
from app.schemas.auth import SignBody, SuccessAuthTokens
from app.schemas.common import Message
from sqlalchemy.exc import IntegrityError

from .router import router


@router.post(
    "/signup",
    responses={
        status.HTTP_409_CONFLICT: {"model": Message},
        status.HTTP_200_OK: {"model": SuccessAuthTokens},
    },
)
async def signup(body: SignBody):
    try:
        user = create_user(body.username, body.password)
        tokens = login_user(user)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Login has been already taken",
        )

    return JSONResponse(tokens)
