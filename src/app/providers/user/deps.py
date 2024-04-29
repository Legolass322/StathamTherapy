from datetime import datetime
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.providers.user.get_user import get_user_by_id
from app.schemas.auth import AuthTokenData
from config.config import config
from logger.logger import logger

from jose import jwt
from pydantic import ValidationError

from database.models.user import User

reuseable_oauth = OAuth2PasswordBearer(tokenUrl="/api/auth/login_form", scheme_name="JWT")


async def get_current_user(token: str = Depends(reuseable_oauth)):
    try:
        payload = jwt.decode(
            token,
            config["auth"]["jwt_secret"],
            algorithms=[config["auth"]["algorithm"]],
        )
        logger.info(payload)
        token_data = AuthTokenData(**payload)
        logger.info(token_data)

        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except ValidationError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user: User = get_user_by_id(token_data.user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )

    return user
