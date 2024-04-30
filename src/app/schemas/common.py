from pydantic import BaseModel


class Message(BaseModel):
    detail: str


class Pagination(BaseModel):
    page_number: int
    page_size: int
