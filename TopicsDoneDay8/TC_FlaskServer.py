from flask import Flask, request, jsonify

app = Flask(__name__)
app.json.sort_keys = False

users_data = [
    {"id": 1, "name": "Alice Johnson", "email": "alice.j@example.com", "role": "Admin", "active": True},
    {"id": 2, "name": "Bob Smith", "email": "bob.smith@example.com", "role": "User", "active": True},
    {"id": 3, "name": "Charlie Davis", "email": "charlie.d@example.com", "role": "User", "active": False},
    {"id": 4, "name": "Diana Prince", "email": "diana.p@example.com", "role": "Moderator", "active": True},
    {"id": 5, "name": "Ethan Hunt", "email": "ethan.h@example.com", "role": "User", "active": True}
]


@app.route("/", methods=["GET"])
def health():
    return jsonify({
        "status": "UP",
        "message": "Flask server is running"
    }), 200


@app.route("/users", methods=["GET"])
def get_users():
    return jsonify({
        "message": "Users fetched successfully",
        "data": users_data
    }), 200


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    user = next((u for u in users_data if u["id"] == user_id), None)
    if not user:
        return jsonify({"message": "User not found"}), 404
    return jsonify(user), 200


@app.route("/users", methods=["POST"])
def create_user():
    body = request.get_json()
    if not body or "name" not in body:
        return jsonify({"message": "Invalid request"}), 400

    new_user = {
        "id": len(users_data)+1,
        "name": body["name"],
        "email": body.get("email", ""),
        "role": body.get("role", "User"),
        "active": True
    }
    users_data.append(new_user)
    return jsonify({
        "message": "User created successfully",
        "data": new_user
    }), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
