from datetime import datetime

from pydantic import BaseModel


class BaseRes(BaseModel):
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime = None
