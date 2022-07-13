from starlette.testclient import TestClient

from app.tests.utils.faker import get_faker
from main import app

faker = get_faker()
client = TestClient(app)


def test_health_check_ok():
    sut = client.get(f"/api/v1/health_check")

    assert sut.status_code == 200
