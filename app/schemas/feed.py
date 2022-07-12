from typing import Optional

from pydantic import Field, BaseModel

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
    id: int = Field(title="id", ge=1)
    nickname: Optional[str] = NICKNAME_FIELD
    title: Optional[str] = TITLE_FIELD
    text: Optional[str] = TEXT_FIELD


class FeedRes(BaseRes):
    id: int
    nickname: str
    password: str
    title: str
    text: str
