import pytest
from config import restaurants, dishes, dish_counter


def create_restaurant(client):
    global restaurants
    rid = max(restaurants.keys(), default=0) + 1
    response = client.post("/api/v1/restaurants", json={
        "name": f"Dish Restaurant {rid}",
        "category": "Veg",
        "location": "Delhi",
        "images": "img.jpg",
        "contact": "123456"
    })
    return response.get_json()["id"]


def test_add_dish_success(client):
    rid = create_restaurant(client)

    response = client.post(f"/api/v1/restaurants/{rid}/dishes", json={
        "name": "Paneer Butter Masala",
        "type": "Main Course",
        "price": 250,
        "available_time": "Lunch",
        "image": "paneer.jpg"
    })

    assert response.status_code == 201
    data = response.get_json()
    assert data["restaurant_id"] == rid
    assert data["enabled"] is True


def test_add_dish_restaurant_not_found(client):
    response = client.post("/api/v1/restaurants/999/dishes", json={
        "name": "Dish",
        "type": "Main",
        "price": 200,
        "available_time": "Lunch",
        "image": "img.jpg"
    })

    assert response.status_code == 404
    assert response.get_json()["error"] == "Restaurant not found"


def test_add_dish_invalid_request(client):
    rid = create_restaurant(client)

    response = client.post(f"/api/v1/restaurants/{rid}/dishes", json={
        "name": "Incomplete Dish"
    })

    assert response.status_code == 400
    assert response.get_json()["error"] == "Invalid request"


def test_update_dish_success(client):
    rid = create_restaurant(client)

    res = client.post(f"/api/v1/restaurants/{rid}/dishes", json={
        "name": "Pizza",
        "type": "Main",
        "price": 300,
        "available_time": "Dinner",
        "image": "pizza.jpg"
    })

    did = res.get_json()["id"]

    response = client.put(f"/api/v1/dishes/{did}", json={"price": 350})

    assert response.status_code == 200
    assert response.get_json()["price"] == 350


def test_update_dish_not_found(client):
    response = client.put("/api/v1/dishes/999", json={"price": 500})

    assert response.status_code == 404
    assert response.get_json()["error"] == "Not found"

def test_change_status_success(client):
    rid = create_restaurant(client)

    res = client.post(f"/api/v1/restaurants/{rid}/dishes", json={
        "name": "Burger",
        "type": "Fast Food",
        "price": 150,
        "available_time": "Evening",
        "image": "burger.jpg"
    })

    did = res.get_json()["id"]

    response = client.put(f"/api/v1/dishes/{did}/status", json={"enabled": False})

    assert response.status_code == 200
    assert response.get_json()["message"] == "Status updated"
    assert dishes[did]["enabled"] is False


def test_change_status_not_found(client):
    response = client.put("/api/v1/dishes/999/status", json={"enabled": False})

    assert response.status_code == 404
    assert response.get_json()["error"] == "Not found"


def test_delete_dish_success(client):
    rid = create_restaurant(client)

    res = client.post(f"/api/v1/restaurants/{rid}/dishes", json={
        "name": "Pasta",
        "type": "Italian",
        "price": 280,
        "available_time": "Dinner",
        "image": "pasta.jpg"
    })

    did = res.get_json()["id"]

    response = client.delete(f"/api/v1/dishes/{did}")

    assert response.status_code == 200
    assert response.get_json()["message"] == "Dish deleted"
    assert did not in dishes


def test_delete_dish_not_found(client):
    response = client.delete("/api/v1/dishes/999")

    assert response.status_code == 404
    assert response.get_json()["error"] == "Not found"
