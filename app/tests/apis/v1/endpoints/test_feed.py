from urllib.parse import urlencode

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

    assert sut.status_code == 200

    _is_list_contains_in_db(sut)
