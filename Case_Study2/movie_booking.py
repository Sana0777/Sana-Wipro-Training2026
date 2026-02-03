# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

movies = []
bookings = []

def get_movie(mid):
    for m in movies:
        if m["id"] == mid:
            return m
    return None

@app.route("/api/movies", methods=["GET"])
def get_movies():
    return jsonify(movies), 200

@app.route("/api/movies/<int:mid>", methods=["GET"])
def get_movie_by_id(mid):
    movie = get_movie(mid)
    if movie is None:
        return jsonify({"error": "Not Found"}), 404
    return jsonify(movie), 200

@app.route("/api/movies", methods=["POST"])
def add_movie():

    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid"}), 400

    if "id" not in data:
        data["id"] = len(movies) + 1

    movies.append(data)

    return jsonify(data), 201


@app.route("/api/movies/<int:mid>", methods=["PUT"])
def update_movie(mid):
    movie = get_movie(mid)

    if movie is None:
        return jsonify({"error": "Not Found"}), 404

    data = request.get_json()

    movie["movie_name"] = data.get("movie_name", movie["movie_name"])
    movie["language"] = data.get("language", movie["language"])
    movie["duration"] = data.get("duration", movie["duration"])
    movie["price"] = data.get("price", movie["price"])

    return jsonify(movie), 200

@app.route("/api/movies/<int:mid>", methods=["DELETE"])
def delete_movie(mid):
    movie = get_movie(mid)

    if movie is None:
        return jsonify({"error": "Not Found"}), 404

    movies.remove(movie)
    return jsonify({"message": "Deleted"}), 200

@app.route("/api/bookings", methods=["POST"])
def book_ticket():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid"}), 400

    movie = get_movie(data.get("movie_id"))

    if movie is None:
        return jsonify({"error": "Not Found"}), 404

    if data.get("tickets") <= 0:
        return jsonify({"error": "Invalid Tickets"}), 400

    total = data["tickets"] * movie["price"]

    booking = {
        "id": len(bookings) + 1,
        "movie": movie["movie_name"],
        "name": data["customer_name"],
        "tickets": data["tickets"],
        "total": total
    }

    bookings.append(booking)

    return jsonify(booking), 201

if __name__ == "__main__":
    app.run()


