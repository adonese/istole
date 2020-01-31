from app import get_location, get_address
import pytest
from app import app


def test_get_location():
    address = get_location("15.5622056666667", "32.5655843333333")
    assert address.raw["address"]["city"] == "الخرطوم"
    assert address.raw["address"]["neighbourhood"] == "الطائف"


def test_get_address():
    address = get_address("15.5622056666667", "32.5655843333333")
    assert address == "الطائف, الخرطوم, ولاية الخرطوم, 11114, السودان \u200eal-Sūdān"


@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            pass
        yield client


def test_send_req_400(client):
    res = client.post("/", json={"lat": 20})
    assert res.status_code == 400


def test_send_req_200(client):
    res = client.post(
        "/",
        json={
            "lat": 20,
            "long": 32,
            "long_describtion": "my long",
            "short_describtion": "short",
        },
    )
    assert res.status_code == 200
    assert res.mimetype == "application/json"


def test_send_req_type(client):
    res = client.post(
        "/",
        json={
            "lat": 20,
            "long": 32,
            "long_describtion": "my long",
            "short_describtion": "short",
        },
    )
    assert res.mimetype == "application/json"


def test_get_without_query(client):
    res = client.get("/get")
    assert res.status_code == 200
    assert res.mimetype == "application/json"
    assert len(res.json()) > 1
