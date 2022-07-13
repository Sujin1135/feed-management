import pytest

from app.schemas.reply import ReplyFindReq, ReplyCreate
from app.services.feed_service import create_feed
from app.services.reply_service import find_replies, create_reply
from app.tests.services.test_feed_service import get_feed_params
from app.tests.utils.faker import get_faker

faker = get_faker()


def get_reply_params(parent_id: int = None) -> ReplyCreate:
    return ReplyCreate(
        nickname=faker.first_name_male(),
        comment=faker.text(),
        parent_id=parent_id,
    )


@pytest.mark.parametrize(
    "limit,offset",
    [
        (20, 0),
        (5, 0),
        (10, 0),
    ]
)
def test_get_and_create_feeds_by_queries(limit, offset):
    feed = create_feed(get_feed_params())
    create_reply(feed.id, get_reply_params())
    create_reply(feed.id, get_reply_params())
    sut = find_replies(feed.id, ReplyFindReq(limit=limit, offset=offset))

    assert len(sut.data) == 2


def test_get_nested_feeds():
    feed = create_feed(get_feed_params())
    created = create_reply(feed.id, get_reply_params())
    create_reply(feed.id, get_reply_params(created.id))
    create_reply(feed.id, get_reply_params(created.id))
    sut = find_replies(feed.id, ReplyFindReq(limit=10, offset=0, parent_id=created.id))

    assert len(sut.data) == 2
