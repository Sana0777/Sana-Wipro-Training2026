from flask import Blueprint, request, jsonify
import config

order_bp = Blueprint("order_bp", __name__)


@order_bp.route("/api/v1/orders", methods=["POST"])
def place_order():
    data = request.get_json()
    required = ["user_id", "restaurant_id", "dishes"]

    if not data or not all(f in data for f in required):
        return jsonify({"error": "Invalid request"}), 400

    user_id = data["user_id"]
    restaurant_id = data["restaurant_id"]
    dish_ids = data["dishes"]

    if user_id not in config.users:
        return jsonify({"error": "Invalid user"}), 400

    if restaurant_id not in config.restaurants:
        return jsonify({"error": "Invalid restaurant"}), 400

    restaurant = config.restaurants[restaurant_id]

    if not restaurant.get("approved"):
        return jsonify({"error": "Restaurant not approved"}), 400

    if restaurant.get("disabled"):
        return jsonify({"error": "Restaurant is disabled"}), 400


    if not isinstance(dish_ids, list) or not dish_ids:
        return jsonify({"error": "Dishes must be a non-empty list"}), 400

    total_price = 0

    for did in dish_ids:
        if did not in config.dishes:
            return jsonify({"error": f"Dish {did} not found"}), 400

        dish = config.dishes[did]

        if dish["restaurant_id"] != restaurant_id:
            return jsonify({"error": f"Dish {did} does not belong to this restaurant"}), 400

        if not dish.get("enabled", True):
            return jsonify({"error": f"Dish {did} is not available"}), 400

        total_price += int(dish["price"])

    config.order_counter += 1
    oid = config.order_counter

    order = {
        "id": oid,
        "user_id": user_id,
        "restaurant_id": restaurant_id,
        "dishes": dish_ids,
        "total_price": total_price,
        "status": "Placed"
    }

    config.orders[oid] = order

    return jsonify(order), 201


@order_bp.route("/api/v1/users/<int:uid>/orders", methods=["GET"])
def orders_by_user(uid):
    result = [o for o in config.orders.values() if o["user_id"] == uid]
    return jsonify(result), 200


@order_bp.route("/api/v1/restaurants/<int:rid>/orders", methods=["GET"])
def orders_by_restaurant(rid):
    result = [o for o in config.orders.values() if o["restaurant_id"] == rid]
    return jsonify(result), 200
