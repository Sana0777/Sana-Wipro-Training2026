import pytest
import config

@pytest.fixture(autouse=True)
def clear_users():
    config.users.clear()
    config.user_counter = 0

def test_register_user_success(client):
    response = client.post("/api/v1/users/register", json={
        "name": "Alice",
        "email": "alice@example.com",
        "password": "secret123"
    })

    assert response.status_code == 201
    data = response.get_json()
    assert "id" in data
    assert data["id"] == 1
    assert data["name"] == "Alice"
    assert data["email"] == "alice@example.com"


def test_register_user_duplicate_email(client):

    client.post("/api/v1/users/register", json={
        "name": "Alice",
        "email": "alice@example.com",
        "password": "secret123"
    })


    response = client.post("/api/v1/users/register", json={
        "name": "Alice2",
        "email": "alice@example.com",
        "password": "secret456"
    })

    assert response.status_code == 409
    assert response.get_json()["error"] == "User exists"


def test_register_user_missing_fields(client):
    response = client.post("/api/v1/users/register", json={
        "name": "Bob",
        "email": "bob@example.com"
        # Missing password
    })

    assert response.status_code == 400
    assert response.get_json()["error"] == "Invalid request"


def test_register_user_empty_body(client):
    response = client.post("/api/v1/users/register", json={})

    assert response.status_code == 400
    assert response.get_json()["error"] == "Invalid request"
