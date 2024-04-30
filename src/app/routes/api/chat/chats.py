from typing import Annotated, List
from fastapi import Depends, Query, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from app.providers.chat.get_user_chats import get_user_chats
from database.models.user import User
from app.providers.user.deps import get_current_user
from .router import router


class ChatModel(BaseModel):
    id: int
    created_at: str


@router.get("/chats", responses={status.HTTP_200_OK: {"model": List[ChatModel]}})
async def get_chats(
    page_number: Annotated[int, Query()],
    page_size: Annotated[int, Query()],
    user: User = Depends(get_current_user),
):
    return JSONResponse(
        [
            ChatModel(chat)
            for chat in get_user_chats(
                user.id, page_number=page_number, page_size=page_size
            )
        ]
    )
