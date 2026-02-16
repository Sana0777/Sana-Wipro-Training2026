import pytest
from config import user_counter, restaurant_counter


def create_user(client):
    global user_counter
    user_counter += 1
    response = client.post("/api/v1/users/register", json={
        "name": f"Order User {user_counter}",
        "email": f"order{user_counter}@test.com",
        "password": "1234"
    })
    return response.get_json()["id"]


def create_restaurant(client):
    global restaurant_counter
    restaurant_counter += 1
    response = client.post("/api/v1/restaurants", json={
        "name": f"Order Restaurant {restaurant_counter}",
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


def test_place_order_success(client):
    uid = create_user(client)
    rid = create_restaurant(client)
    did = create_dish(client, rid)

    response = client.post("/api/v1/orders", json={
        "user_id": uid,
        "restaurant_id": rid,
        "dishes": [did]
    })

    assert response.status_code == 201
    data = response.get_json()
    assert data["user_id"] == uid
    assert data["restaurant_id"] == rid
    assert data["status"] == "Placed"
    assert data["total_price"] == 200


def test_place_order_invalid_request(client):
    response = client.post("/api/v1/orders", json={
        "user_id": 1
    })

    assert response.status_code == 400
    assert response.get_json()["error"] == "Invalid request"


def test_place_order_invalid_user(client):
    rid = create_restaurant(client)
    did = create_dish(client, rid)

    response = client.post("/api/v1/orders", json={
        "user_id": 999,
        "restaurant_id": rid,
        "dishes": [did]
    })

    assert response.status_code == 400
    assert response.get_json()["error"] == "Invalid user"


def test_orders_by_user_empty(client):
    response = client.get("/api/v1/users/999/orders")
    assert response.status_code == 200
    assert response.get_json() == []


def test_orders_by_user_with_data(client):
    uid = create_user(client)
    rid = create_restaurant(client)
    did = create_dish(client, rid)

    client.post("/api/v1/orders", json={
        "user_id": uid,
        "restaurant_id": rid,
        "dishes": [did]
    })

    response = client.get(f"/api/v1/users/{uid}/orders")
    assert response.status_code == 200
    assert len(response.get_json()) == 1


def test_orders_by_restaurant_empty(client):
    response = client.get("/api/v1/restaurants/999/orders")
    assert response.status_code == 200
    assert response.get_json() == []


def test_orders_by_restaurant_with_data(client):
    uid = create_user(client)
    rid = create_restaurant(client)
    did = create_dish(client, rid)

    client.post("/api/v1/orders", json={
        "user_id": uid,
        "restaurant_id": rid,
        "dishes": [did]
    })

    response = client.get(f"/api/v1/restaurants/{rid}/orders")
    assert response.status_code == 200
    assert len(response.get_json()) == 1
