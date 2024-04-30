from http.client import HTTPException
from fastapi import Depends, status

from app.providers.chat.check_user_has_chat import check_user_has_chat
from app.providers.chat.get_chat_messages import get_chat_messages
from app.providers.chat.put_message import put_message
from app.schemas.chat import SendMessageBody
from app.schemas.common import Message as HTTPMessage, Pagination
from database.models.message import Message
from database.models.user import User
from app.providers.user.deps import get_current_user
from .router import router


@router.post("/send_message", responses={status.HTTP_403_FORBIDDEN: {"model": HTTPMessage}})
async def send_message(
    body: SendMessageBody, user: User = Depends(get_current_user)
):
    if not check_user_has_chat(user.id, body.chat_id):
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="No such chat")
    
    put_message(user.id, body.chat_id, body.text)

    return status.HTTP_200_OK
