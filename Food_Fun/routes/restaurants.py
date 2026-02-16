from flask import Blueprint, request, jsonify
import config

restaurant_bp = Blueprint("restaurant_bp", __name__)

@restaurant_bp.route("/api/v1/restaurants", methods=["POST"])
def register_restaurant():
    data = request.get_json()
    required = ["name", "category", "location", "images", "contact"]

    if not data or not all(f in data for f in required):
        return jsonify({"error": "Invalid request"}), 400

    for r in config.restaurants.values():
        if r["name"] == data["name"]:
            return jsonify({"error": "Restaurant exists"}), 409

    config.restaurant_counter += 1
    rid = config.restaurant_counter

    restaurant = {"id": rid, "approved": False, "disabled": False, **data}
    config.restaurants[rid] = restaurant

    return jsonify(restaurant), 201


@restaurant_bp.route("/api/v1/restaurants/<int:rid>", methods=["GET"])
def view_restaurant(rid):
    if rid not in config.restaurants:
        return jsonify({"error": "Not found"}), 404
    return jsonify(config.restaurants[rid]), 200


@restaurant_bp.route("/api/v1/restaurants/<int:rid>", methods=["PUT"])
def update_restaurant(rid):
    if rid not in config.restaurants:
        return jsonify({"error": "Not found"}), 404

    config.restaurants[rid].update(request.get_json())
    return jsonify(config.restaurants[rid]), 200


@restaurant_bp.route("/api/v1/restaurants/<int:rid>/disable", methods=["PUT"])
def disable_restaurant(rid):
    if rid not in config.restaurants:
        return jsonify({"error": "Not found"}), 404

    config.restaurants[rid]["disabled"] = True
    return jsonify({"message": "Restaurant disabled"}), 200

@restaurant_bp.route("/api/v1/restaurants", methods=["GET"])
def get_all_restaurants():
    return jsonify(list(config.restaurants.values())), 200


@restaurant_bp.route("/api/v1/restaurants/search", methods=["GET"])
def search_restaurants():
    name = request.args.get("name", "")
    location = request.args.get("location", "")

    result = [
        r for r in config.restaurants.values()
        if name.lower() in r["name"].lower()
        and location.lower() in r["location"].lower()
    ]

    return jsonify(result), 200
