from datetime import datetime
from typing import Optional


class BaseRes:
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]
