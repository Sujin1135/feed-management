from app.crud.crud_base import CRUDBase
from app.models.feed import Feed
from app.schemas.feed import FeedCreate, FeedUpdate


class CRUDFeed(CRUDBase[Feed, FeedCreate, FeedUpdate]):
    """Feed repository"""


crud_feed = CRUDFeed(Feed)
