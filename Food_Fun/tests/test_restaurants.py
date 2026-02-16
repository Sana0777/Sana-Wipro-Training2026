import pytest
import config

def test_register_restaurant(client):
    response = client.post("/api/v1/restaurants", json={
        "name": "Food Hub",
        "category": "Indian",
        "location": "Delhi",
        "images": "img.jpg",
        "contact": "1234567890"
    })
    assert response.status_code == 201
    data = response.get_json()
    assert "id" in data

    assert data["id"] == config.restaurant_counter


def test_register_duplicate_restaurant(client):
    client.post("/api/v1/restaurants", json={
        "name": "Food Hub",
        "category": "Indian",
        "location": "Delhi",
        "images": "img.jpg",
        "contact": "123"
    })

    response = client.post("/api/v1/restaurants", json={
        "name": "Food Hub",
        "category": "Indian",
        "location": "Delhi",
        "images": "img.jpg",
        "contact": "123"
    })

    assert response.status_code == 409
    assert response.get_json()["error"] == "Restaurant exists"


def test_view_restaurant(client):
    res = client.post("/api/v1/restaurants", json={
        "name": "Test",
        "category": "Veg",
        "location": "Mumbai",
        "images": "img",
        "contact": "123"
    })
    rid = res.get_json()["id"]

    response = client.get(f"/api/v1/restaurants/{rid}")
    assert response.status_code == 200
    data = response.get_json()
    assert data["id"] == rid


def test_search_restaurant(client):
    client.post("/api/v1/restaurants", json={
        "name": "Pizza Place",
        "category": "Italian",
        "location": "Delhi",
        "images": "img",
        "contact": "123"
    })

    response = client.get("/api/v1/restaurants/search?name=Pizza")
    assert response.status_code == 200
    results = response.get_json()
    assert any("Pizza" in r["name"] for r in results)


def test_update_restaurant(client):
    res = client.post("/api/v1/restaurants", json={
        "name": "UpdateTest",
        "category": "Veg",
        "location": "Delhi",
        "images": "img",
        "contact": "123"
    })
    rid = res.get_json()["id"]

    response = client.put(f"/api/v1/restaurants/{rid}", json={"location": "Noida"})
    assert response.status_code == 200
    data = response.get_json()
    assert data["location"] == "Noida"


def test_disable_restaurant(client):
    res = client.post("/api/v1/restaurants", json={
        "name": "DisableTest",
        "category": "Veg",
        "location": "Delhi",
        "images": "img",
        "contact": "123"
    })
    rid = res.get_json()["id"]

    response = client.put(f"/api/v1/restaurants/{rid}/disable")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Restaurant disabled"
