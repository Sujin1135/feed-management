import pytest

from app.exceptions.not_found_error import NotFoundError
from app.exceptions.unauthorized_error import UnauthorizedError
from app.models.feed import Feed
from app.schemas.feed import FeedCreate, FeedUpdate, FeedDelete, FeedFindReq
from app.services.feed_service import create_feed, update_feed, soft_remove_feed, get_feed, find_feeds
from app.tests.utils.faker import get_faker

faker = get_faker()


def get_feed_params() -> FeedCreate:
    return FeedCreate(
        title=faker.name(),
        text=faker.text(),
        nickname=faker.first_name_male(),
        password="pwd1234!",
    )


def _convert_model_to_update_feed(model: Feed, password: str) -> FeedUpdate:
    return FeedUpdate(
        title=faker.last_name(),
        text=faker.text(),
        nickname=model.nickname,
        password=password,
    )


def test_create_feed_data_correctly():
    data = get_feed_params()
    sut = create_feed(data)

    assert data.title == sut.title
    assert data.text == sut.text
    assert data.nickname == sut.nickname


def test_update_feed_data_correctly():
    data = get_feed_params()
    password = data.password
    created = create_feed(data)
    created.title = faker.last_name()
    params = _convert_model_to_update_feed(created, password)
    sut = update_feed(created.id, params)

    assert params.title == sut.title
    assert params.text == sut.text
    assert params.nickname == sut.nickname


def test_remove_feed_to_update_deleted_at():
    data = get_feed_params()
    password = data.password
    created = create_feed(data)
    soft_remove_feed(created.id, FeedDelete(password=password))

    with pytest.raises(NotFoundError):
        get_feed(created.id)


def test_occur_unauthorized_error_when_update_feed():
    data = get_feed_params()
    invalid_password = faker.name()
    created = create_feed(data)
    params = _convert_model_to_update_feed(created, invalid_password)

    with pytest.raises(UnauthorizedError):
        update_feed(created.id, params)


def test_occur_unauthorized_error_when_delete_feed():
    data = get_feed_params()
    invalid_password = faker.name()
    created = create_feed(data)

    with pytest.raises(UnauthorizedError):
        soft_remove_feed(created.id, FeedDelete(password=invalid_password))


@pytest.mark.parametrize(
    "limit,offset,order_by,nickname,title",
    [
        (20, 0, None, None, None),
        (10, 0, "DESC_ID", "", ""),
        (10, 0, "DESC_ID", faker.first_name_male(), ""),
    ]
)
def test_get_feeds_by_queries(limit, offset, order_by, nickname, title):
    params = FeedFindReq(
        limit=limit,
        offset=offset,
        order_by=order_by,
        nickname=nickname,
        title=title,
    )
    sut = find_feeds(params)

    assert sut.count >= 0
