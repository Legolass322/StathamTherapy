from http.client import HTTPException
from typing import Annotated
from fastapi import Depends, Query, status
from fastapi.responses import JSONResponse

from app.providers.chat.check_user_has_chat import check_user_has_chat
from app.providers.chat.get_chat_messages import get_chat_messages
from app.schemas.common import Message as HTTPMessage
from database.models.message import Message
from database.models.user import User
from app.providers.user.deps import get_current_user
from .router import router


@router.get(
    "/messages",
    responses={
        status.HTTP_200_OK: {"array": Message},
        status.HTTP_403_FORBIDDEN: {"model": HTTPMessage},
    },
)
async def get_messages(
    chat_id: Annotated[int, Query()],
    page_number: Annotated[int, Query()],
    page_size: Annotated[int, Query()],
    user: User = Depends(get_current_user),
):
    if not check_user_has_chat(user.id, chat_id):
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="No such chat")

    return JSONResponse([m.to_json() for m in get_chat_messages(chat_id, page_size, page_number)])
