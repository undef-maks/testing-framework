import pytest
from utils.api_client import APIClient

@pytest.fixture(scope="module")
def api_client():
    return APIClient()

def test_get_posts(api_client):
    response = api_client.get("/posts/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data

def test_post_create(api_client):
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = api_client.post("/posts", data=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "foo"
    assert data["id"] == 101  

def test_put_update(api_client):
    payload = {
        "id": 1,
        "title": "updated title",
        "body": "updated body",
        "userId": 1
    }
    response = api_client.put("/posts/1", data=payload)
    assert response.status_code == 200
    assert response.json()["title"] == "updated title"

def test_delete_post(api_client):
    response = api_client.delete("/posts/1")
    assert response.status_code == 200
