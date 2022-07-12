from typing import Optional

from pydantic import Field, BaseModel

from app.models.feed import Feed
from app.schemas.base import BaseRes

NICKNAME_FIELD = Field(title="nickname", max_length=50)
PASSWORD_FIELD = Field(title="password", min_length=8, max_length=16)
TITLE_FIELD = Field(title="nickname", min_length=2, max_length=100)
TEXT_FIELD = Field(title="title", max_length=2000)


class FeedCreate(BaseModel):
    nickname: str = NICKNAME_FIELD
    password: str = PASSWORD_FIELD
    title: str = TITLE_FIELD
    text: str = TEXT_FIELD


class FeedUpdate(BaseModel):
    nickname: Optional[str] = NICKNAME_FIELD
    title: Optional[str] = TITLE_FIELD
    text: Optional[str] = TEXT_FIELD
    password: str = PASSWORD_FIELD


class FeedDelete(BaseModel):
    password: str = PASSWORD_FIELD


class FeedRes(BaseRes):
    def __init__(self, model: Feed):
        self.id = model.id
        self.nickname = model.nickname
        self.title = model.title
        self.text = model.text
        self.created_at = model.created_at
        self.updated_at = model.updated_at
        self.deleted_at = model.deleted_at

    id: int
    nickname: str
    title: str
    text: str


class FeedFindReq(BaseModel):
    limit: Optional[int] = Field(50, title="limit", ge=1)
    offset: Optional[int] = Field(0, title="offset", ge=0)
    order_by: Optional[str] = Field(title="order_by")
    nickname: Optional[str] = Field(title="nickname", max_length=50)
    title: Optional[str] = Field(title="title", max_length=100)
