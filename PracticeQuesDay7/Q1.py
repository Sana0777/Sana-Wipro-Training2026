from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
users = [
    {"id": 1, "name": "Sana"},
    {"id": 2, "name": "Rashmi"}
]

@app.route("/", methods=["GET"])
def home():
    return "Welcome to User API"

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user)
    return jsonify({"message": "User not found"}), 404


@app.route("/users", methods=["POST"])
def add_user():
    data=request.json
    new_user={
        "id":len(users)+1,"name":data.get("name")
    }
    users.append(new_user)
    return jsonify(new_user),201


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json

    if not data or "name" not in data:
        return jsonify({"message": "Name is required"}), 400

    for user in users:
        if user["id"] == user_id:
            user["name"] = data["name"]
            return jsonify(user)

    return jsonify({"message": "User not found"}), 404


@app.route("/users/<int:user_id>", methods=["PATCH"])
def patch_user(user_id):
    data = request.json

    for user in users:
        if user["id"] == user_id:
            if "name" in data:
                user["name"] = data["name"]
            return jsonify(user)

    return jsonify({"message": "User not found"}), 404


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return jsonify({"message": "User deleted successfully"})

    return jsonify({"message": "User not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
