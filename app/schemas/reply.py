from typing import Optional

from pydantic import Field, BaseModel

from app.models.reply import Reply
from app.schemas.base import BaseRes
from app.schemas.feed import NICKNAME_FIELD

FEED_ID = Field(title="feed_id")
COMMENT_FIELD = Field(title="comment", min_length=1, max_length=255)
PARENT_ID_FIELD = Field(0, title="parent_id", ge=0)
DEPTH_ID_FIELD = Field(0, title="depth", ge=0)


class ReplyCreate(BaseModel):
    feed_id: Optional[int] = FEED_ID
    parent_id: Optional[int] = PARENT_ID_FIELD
    depth: Optional[int] = DEPTH_ID_FIELD
    nickname: str = NICKNAME_FIELD
    comment: str = COMMENT_FIELD


class ReplyUpdate(BaseModel):
    feed_id: Optional[int] = FEED_ID
    comment: Optional[str] = COMMENT_FIELD


class ReplyFindRes(BaseModel):
    count: int
    data: list


class ReplyFindReq(BaseModel):
    limit: Optional[int] = Field(50, title="limit", ge=1)
    offset: Optional[int] = Field(0, title="offset", ge=0)
    parent_id: Optional[int] = Field(title="parent_id", ge=0)
    depth: Optional[int] = Field(0, title="depth", ge=0)


class ReplyRes(BaseRes):

    @staticmethod
    def create_by_model(model: Reply):
        return ReplyRes(
            id=model.id,
            feed_id=model.feed_id,
            parent_id=model.parent_id,
            nickname=model.nickname,
            depth=model.depth,
            comment=model.comment,
            created_at=model.created_at,
            updated_at=model.updated_at,
            deleted_at=model.deleted_at,
        )

    id: int
    feed_id: int
    parent_id: Optional[int]
    nickname: str
    depth: int
    comment: str
