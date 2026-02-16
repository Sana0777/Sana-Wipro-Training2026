import config
from flask import Blueprint, request, jsonify

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/api/v1/users/register", methods=["POST"])
def register_user():
    data = request.get_json()
    required = ["name", "email", "password"]

    if not data or not all(f in data for f in required):
        return jsonify({"error": "Invalid request"}), 400

    for u in config.users.values():
        if u["email"] == data["email"]:
            return jsonify({"error": "User exists"}), 409

    config.user_counter += 1
    uid = config.user_counter

    user = {"id": uid, **data}
    config.users[uid] = user

    return jsonify(user), 201
