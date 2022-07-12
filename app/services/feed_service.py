from app.crud.crud_feed import crud_feed
from app.models.feed import Feed
from app.schemas.feed import FeedCreate, FeedUpdate


def get_feed(feed_id: int) -> Feed:
    return crud_feed.get(feed_id)


def create_feed(data: FeedCreate) -> Feed:
    return crud_feed.create(data)


def update_feed(data: FeedUpdate) -> Feed:
    return crud_feed.update(data.id, data)


def soft_remove_feed(feed_id: int) -> None:
    crud_feed.soft_remove(feed_id)
