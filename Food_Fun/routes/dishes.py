from flask import Blueprint, request, jsonify
import config

dish_bp = Blueprint("dish_bp", __name__)


@dish_bp.route("/api/v1/restaurants/<int:rid>/dishes", methods=["POST"])
def add_dish(rid):
    if rid not in config.restaurants:
        return jsonify({"error": "Restaurant not found"}), 404

    data = request.get_json()
    required = ["name", "type", "price", "available_time", "image"]

    if not data or not all(f in data for f in required):
        return jsonify({"error": "Invalid request"}), 400

    config.dish_counter += 1
    did = config.dish_counter

    dish = {"id": did, "restaurant_id": rid, "enabled": True, **data}
    config.dishes[did] = dish

    return jsonify(dish), 201


@dish_bp.route("/api/v1/dishes/<int:did>", methods=["PUT"])
def update_dish(did):
    if did not in config.dishes:
        return jsonify({"error": "Not found"}), 404

    config.dishes[did].update(request.get_json())
    return jsonify(config.dishes[did]), 200


@dish_bp.route("/api/v1/dishes/<int:did>/status", methods=["PUT"])
def change_status(did):
    if did not in config.dishes:
        return jsonify({"error": "Not found"}), 404

    config.dishes[did]["enabled"] = request.json.get("enabled", True)
    return jsonify({"message": "Status updated"}), 200

@dish_bp.route("/api/v1/dishes/<int:did>", methods=["DELETE"])
def delete_dish(did):
    if did not in config.dishes:
        return jsonify({"error": "Not found"}), 404

    del config.dishes[did]
    return jsonify({"message": "Dish deleted"}), 200
