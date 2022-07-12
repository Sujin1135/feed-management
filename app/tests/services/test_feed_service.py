import pytest

from app.exceptions.not_found_error import NotFoundError
from app.models.feed import Feed
from app.schemas.feed import FeedCreate, FeedUpdate
from app.services.feed_service import create_feed, update_feed, soft_remove_feed, get_feed
from app.tests.utils.faker import get_faker

faker = get_faker()


def _get_params() -> FeedCreate:
    return FeedCreate(
        title=faker.name(),
        text=faker.text(),
        nickname=faker.first_name_male(),
        password="pwd1234!",
    )


def _convert_model_to_update_feed(model: Feed) -> FeedUpdate:
    return FeedUpdate(
        id=model.id,
        title=faker.last_name(),
        text=faker.text(),
        nickname=model.nickname,
    )


def test_create_feed_data_correctly():
    data = _get_params()
    sut = create_feed(data)

    assert data.title == sut.title
    assert data.text == sut.text
    assert data.nickname == sut.nickname


def test_update_feed_data_correctly():
    data = _get_params()
    created = create_feed(data)
    created.title = faker.last_name()
    params = _convert_model_to_update_feed(created)
    sut = update_feed(params)

    assert params.title == sut.title
    assert params.text == sut.text
    assert params.nickname == sut.nickname
    assert params.id == sut.id


def test_remove_feed_to_update_deleted_at():
    created = create_feed(_get_params())
    soft_remove_feed(created.id)

    with pytest.raises(NotFoundError):
        get_feed(created.id)
