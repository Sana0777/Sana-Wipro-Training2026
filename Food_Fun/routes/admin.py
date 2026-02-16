from flask import Blueprint, jsonify
from config import restaurants, orders, feedbacks

admin_bp = Blueprint("admin_bp", __name__)

@admin_bp.route("/api/v1/admin/restaurants/<rid>/approve", methods=["PUT"])
def approve_restaurant(rid):
    rid = int(rid)
    if rid not in restaurants:
        return jsonify({"error": "Not found"}), 404

    restaurants[rid]["approved"] = True
    return jsonify({"message": "Restaurant approved"}), 200


@admin_bp.route("/api/v1/admin/restaurants/<rid>/disable", methods=["PUT"])
def disable_restaurant_admin(rid):
    rid = int(rid)
    if rid not in restaurants:
        return jsonify({"error": "Not found"}), 404

    restaurants[rid]["disabled"] = True
    return jsonify({"message": "Restaurant disabled"}), 200


@admin_bp.route("/api/v1/admin/orders", methods=["GET"])
def view_orders():
    return jsonify(list(orders.values())), 200


@admin_bp.route("/api/v1/admin/feedback", methods=["GET"])
def view_feedback():
    return jsonify(feedbacks), 200
