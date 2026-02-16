from flask import Blueprint, request, jsonify
import config

rating_bp = Blueprint("rating_bp", __name__)

@rating_bp.route("/api/v1/ratings", methods=["POST"])
def give_rating():
    data = request.get_json()

    required = ["order_id", "rating", "comment"]

    if not data:
        return jsonify({"error": "Invalid request"}), 400

    if not all(field in data for field in required):
        return jsonify({"error": "Invalid request"}), 400

    if data["order_id"] not in config.orders:
        return jsonify({"error": "Invalid order"}), 400

    config.rating_counter += 1
    rid = config.rating_counter

    rating = {
        "id": rid,
        "order_id": data["order_id"],
        "rating": data["rating"],
        "comment": data["comment"]
    }

    config.ratings[rid] = rating
    config.feedbacks.append(rating)

    return jsonify(rating), 201
