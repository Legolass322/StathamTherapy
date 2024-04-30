from pydantic import BaseModel

from app.schemas.common import Pagination


class SendMessageBody(BaseModel):
    chat_id: int
    text: str


class GetMessagesParams(Pagination):
    chat_id: int
