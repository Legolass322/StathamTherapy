from http.client import HTTPException
from fastapi import Depends, status

from app.providers.chat.check_user_has_chat import check_user_has_chat
from app.providers.chat.put_message import put_message
from app.schemas.chat import SendMessageBody
from app.schemas.common import Message as HTTPMessage
from database.models.user import User
from app.providers.user.deps import get_current_user
from .router import router

from statham.user import statham_user


async def handle_statham_message(chat_id: int, message: str):
    if check_user_has_chat(statham_user.user_id, chat_id):
        statham_user.reply(chat_id, message)


@router.post(
    "/send_message", responses={status.HTTP_403_FORBIDDEN: {"model": HTTPMessage}}
)
async def send_message(body: SendMessageBody, user: User = Depends(get_current_user)):
    if not check_user_has_chat(user.id, body.chat_id):
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="No such chat")

    put_message(user.id, body.chat_id, body.text)

    handle_statham_message(body.chat_id, body.text)

    return status.HTTP_200_OK
