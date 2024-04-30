from typing import List
from fastapi import Depends, status
from fastapi.responses import JSONResponse
from pydantic import TypeAdapter

from app.providers.chat.get_user_chats import get_user_chats
from app.schemas.common import Pagination
from database.models.chat import Chat
from database.models.user import User
from app.providers.user.deps import get_current_user
from .router import router


@router.get("/chats", responses={status.HTTP_200_OK: {"array": Chat}})
async def get_chats(pagination: Pagination, user: User = Depends(get_current_user)):
    return JSONResponse(get_user_chats(user.id, **pagination))
