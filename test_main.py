from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_shorten_url():
    response = client.post(
        "/shorten",
        json={"url": "https://www.google.com/"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "short_code" in data
    assert "short_url" in data


def test_redirect_url():
    response = client.post(
        "/shorten",
        json={"url": "https://www.google.com/"}
    )
    short_code = response.json()["short_code"]

    redirect_response = client.get(
        f"/{short_code}",
        follow_redirects=False
    )
    assert redirect_response.status_code == 307
    assert redirect_response.headers["location"] == "https://www.google.com/"


def test_invalid_short_code():
    response = client.get(
        "/invalid123",
        follow_redirects=False
    )
    assert response.status_code == 404

def test_invalid_url():
    response = client.post(
        "/shorten",
        json={"url": "not-a-valid-url"}
    )

    assert response.status_code == 422    