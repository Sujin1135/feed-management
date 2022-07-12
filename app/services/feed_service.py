from app.core.auth import gen_hashed_password, validate_password
from app.crud.crud_feed import crud_feed
from app.models.feed import Feed
from app.schemas.feed import FeedCreate, FeedUpdate, FeedDelete


def get_feed(feed_id: int) -> Feed:
    return crud_feed.get(feed_id)


def create_feed(data: FeedCreate) -> Feed:
    data.password = gen_hashed_password(data.password)
    return crud_feed.create(data)


def update_feed(feed_id: int, data: FeedUpdate) -> Feed:
    validate_password(data.password, crud_feed.get(feed_id).password)
    data.password = None
    return crud_feed.update(feed_id, data)


def soft_remove_feed(feed_id: int, data: FeedDelete) -> None:
    validate_password(data.password, crud_feed.get(feed_id).password)
    crud_feed.soft_remove(feed_id)
