import pytest
from config import restaurants, orders, feedbacks, restaurant_counter


def create_restaurant(client):
    global restaurant_counter
    restaurant_counter += 1
    rid = restaurant_counter  # Auto-increment integer ID
    response = client.post("/api/v1/restaurants", json={
        "name": f"Admin Test Restaurant {rid}",
        "category": "Veg",
        "location": "Delhi",
        "images": "img.jpg",
        "contact": "123456"
    })
    return response.get_json()["id"]


def test_approve_restaurant_success(client):
    rid = create_restaurant(client)

    response = client.put(f"/api/v1/admin/restaurants/{rid}/approve")

    assert response.status_code == 200
    assert response.get_json()["message"] == "Restaurant approved"
    assert restaurants[rid]["approved"] is True


def test_approve_restaurant_not_found(client):
    response = client.put("/api/v1/admin/restaurants/999/approve")  # Non-existent ID

    assert response.status_code == 404
    assert response.get_json()["error"] == "Not found"



def test_disable_restaurant_success(client):
    rid = create_restaurant(client)

    response = client.put(f"/api/v1/admin/restaurants/{rid}/disable")

    assert response.status_code == 200
    assert response.get_json()["message"] == "Restaurant disabled"
    assert restaurants[rid]["disabled"] is True


def test_disable_restaurant_not_found(client):
    response = client.put("/api/v1/admin/restaurants/999/disable")  # Non-existent ID

    assert response.status_code == 404
    assert response.get_json()["error"] == "Not found"


def test_view_orders_empty(client):
    orders.clear()
    response = client.get("/api/v1/admin/orders")

    assert response.status_code == 200
    assert response.get_json() == []


def test_view_orders_with_data(client):
    orders.clear()
    orders[1] = {
        "id": 1,
        "user_id": 1,
        "restaurant_id": 1,
        "status": "Placed"
    }

    response = client.get("/api/v1/admin/orders")

    assert response.status_code == 200
    assert len(response.get_json()) == 1


def test_view_feedback_empty(client):
    feedbacks.clear()
    response = client.get("/api/v1/admin/feedback")

    assert response.status_code == 200
    assert response.get_json() == []


def test_view_feedback_with_data(client):
    feedbacks.clear()
    feedbacks.append({
        "id": 1,
        "order_id": 1,
        "rating": 5,
        "comment": "Excellent"
    })

    response = client.get("/api/v1/admin/feedback")

    assert response.status_code == 200
    assert len(response.get_json()) == 1
