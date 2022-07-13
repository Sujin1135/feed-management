from app.crud.crud_base import CRUDBase
from app.models.keyword import Keyword
from app.schemas.keyword import KeywordCreate, KeywordUpdate


class CRUDKeyword(CRUDBase[Keyword, KeywordCreate, KeywordUpdate]):
    """Keyword repository"""
