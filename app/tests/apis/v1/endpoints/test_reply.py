from urllib.parse import urlencode

from starlette import status
from starlette.testclient import TestClient

from app.services.feed_service import create_feed
from app.services.reply_service import create_reply
from app.tests.services.test_feed_service import get_feed_params
from app.tests.services.test_reply_service import get_reply_params
from app.tests.utils.faker import get_faker
from main import app

faker = get_faker()
client = TestClient(app)


def test_create_replies_by_feed_id():
    feed = create_feed(get_feed_params())
    sut = client.post(f"/api/v1/feeds/{feed.id}/replies", json=get_reply_params().dict())

    assert sut.status_code == status.HTTP_201_CREATED


def _request_find(feed_id: int, params={}):
    return client.get(f"/api/v1/feeds/{feed_id}/replies?{urlencode(params)}")


def test_get_replies_by_feed_id():
    feed = create_feed(get_feed_params())
    create_reply(feed.id, get_reply_params())
    create_reply(feed.id, get_reply_params())

    sut = _request_find(feed.id, {"limit": 10, "offset": 0})
    assert sut.status_code == status.HTTP_200_OK


def test_get_nested_replies_by_feed_id():
    feed = create_feed(get_feed_params())
    root_reply = create_reply(feed.id, get_reply_params())
    create_reply(feed.id, get_reply_params(root_reply.id))
    create_reply(feed.id, get_reply_params(root_reply.id))

    sut = _request_find(feed.id, {"limit": 10, "offset": 0, "parent_id": root_reply.id})
    result = sut.json()

    assert sut.status_code == status.HTTP_200_OK
    assert len(result["data"]) == 2
