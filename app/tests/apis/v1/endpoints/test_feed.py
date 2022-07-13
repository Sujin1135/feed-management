from urllib.parse import urlencode

import pytest
from starlette import status
from starlette.testclient import TestClient

from app.crud.crud_feed import crud_feed
from app.tests.utils.faker import get_faker
from main import app

faker = get_faker()
client = TestClient(app)


def _request_find(params={}):
    return client.get(f"/api/v1/feeds?{urlencode(params)}")


def _is_list_contains_in_db(sut):
    result = sut.json()["data"]
    expected = crud_feed.find(limit=50, offset=0)
    for result_data, expected_data in zip(result, expected):
        assert result_data["id"] == expected_data.id


def test_return_feeds_by_queries():
    params = {"something": "unnecessary"}
    sut = _request_find(params=params)

    assert sut.status_code == status.HTTP_200_OK

    _is_list_contains_in_db(sut)


def _make_create_params() -> dict:
    return {
        "title": faker.name(),
        "text": faker.text(),
        "nickname": faker.first_name_male(),
        "password": "test1234!",
    }


def _request_create(data: dict):
    return client.post("/api/v1/feeds", json=data)


def test_create_feed_correctly():
    sut = _request_create(_make_create_params())
    assert sut.status_code == status.HTTP_201_CREATED


def test_create_duplicated_nickname():
    data = _make_create_params()
    _request_create(data)
    sut = _request_create(data)
    assert sut.status_code == status.HTTP_201_CREATED


def test_create_with_invalid_password():
    data = _make_create_params()
    data["password"] = "12345678901234567"
    sut = _request_create(data)
    assert sut.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def _request_update(feed_id: int, data: dict):
    return client.patch(f"/api/v1/feeds/{feed_id}", json=data)


def test_update_correctly():
    params = _make_create_params()
    create_result = _request_create(params)
    data = create_result.json()
    text = "change text"

    sut = _request_update(data["id"], {"text": text, "password": params["password"]})
    assert sut.status_code == status.HTTP_200_OK


def test_update_with_invalid_password():
    create_result = _request_create(_make_create_params())
    data = create_result.json()
    text = "change text"

    sut = _request_update(data["id"], {"text": text, "password": "invalid_pwd"})
    assert sut.status_code == status.HTTP_401_UNAUTHORIZED


def _request_delete(feed_id: int, password: str):
    return client.patch(f"/api/v1/feeds/{feed_id}/remove", json={"password": password})


def test_delete_correctly():
    params = _make_create_params()
    create_result = _request_create(params)
    data = create_result.json()
    sut = _request_delete(data["id"], params["password"])

    assert sut.status_code == status.HTTP_200_OK


def test_delete_with_invalid_password():
    create_result = _request_create(_make_create_params())
    data = create_result.json()
    sut = _request_delete(data["id"], "invalid password")

    assert sut.status_code == status.HTTP_401_UNAUTHORIZED
