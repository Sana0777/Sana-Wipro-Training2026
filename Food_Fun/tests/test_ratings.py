import pytest
from config import ratings, feedbacks


def create_user(client):
    response = client.post("/api/v1/users/register", json={
        "name": "Rating User",
        "email": "rating@test.com",
        "password": "1234"
    })
    return response.get_json()["id"]


def create_restaurant(client):
    response = client.post("/api/v1/restaurants", json={
        "name": "Rating Restaurant",
        "category": "Veg",
        "location": "Delhi",
        "images": "img.jpg",
        "contact": "123456"
    })
    rid = response.get_json()["id"]


    client.put(f"/api/v1/admin/restaurants/{rid}/approve")

    return rid


def create_dish(client, rid):
    response = client.post(f"/api/v1/restaurants/{rid}/dishes", json={
        "name": "Paneer",
        "type": "Main",
        "price": 200,
        "available_time": "Lunch",
        "image": "paneer.jpg"
    })
    return response.get_json()["id"]


def create_order(client):
    uid = create_user(client)
    rid = create_restaurant(client)
    did = create_dish(client, rid)

    response = client.post("/api/v1/orders", json={
        "user_id": uid,
        "restaurant_id": rid,
        "dishes": [did]
    })

    return response.get_json()["id"]


def test_give_rating_success(client):
    order_id = create_order(client)

    response = client.post("/api/v1/ratings", json={
        "order_id": order_id,
        "rating": 5,
        "comment": "Excellent food!"
    })

    assert response.status_code == 201

    data = response.get_json()
    assert data["order_id"] == order_id
    assert data["rating"] == 5
    assert data["comment"] == "Excellent food!"
    assert "id" in data

    assert data["id"] in ratings
    assert data in feedbacks


def test_give_rating_missing_fields(client):
    response = client.post("/api/v1/ratings", json={
        "order_id": 999,
        "rating": 5
    })

    assert response.status_code == 400
    assert response.get_json()["error"] == "Invalid request"


def test_give_rating_empty_body(client):
    response = client.post("/api/v1/ratings", json={})

    assert response.status_code == 400
    assert response.get_json()["error"] == "Invalid request"


def test_give_rating_no_json(client):
    response = client.post("/api/v1/ratings", json={})
    assert response.status_code == 400
    assert response.get_json()["error"] == "Invalid request"
