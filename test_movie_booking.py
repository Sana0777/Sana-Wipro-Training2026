import pytest
import requests

BASE = "http://127.0.0.1:5000"


@pytest.fixture(scope="module")
def setup_movie():
    movie = {
        "id": 101,
        "movie_name": "Interstellar",
        "language": "English",
        "duration": "2h 49m",
        "price": 250
    }

    try:
        requests.post(f"{BASE}/api/movies", json=movie)
    except Exception:
        pass

    yield movie

    try:
        requests.delete(f"{BASE}/api/movies/101")
    except Exception:
        pass



def test_get_movies():
    try:
        r = requests.get(f"{BASE}/api/movies")
        assert r.status_code == 200
    except Exception:
        assert False


@pytest.mark.parametrize("movie", [
    {
        "id": 102,
        "movie_name": "3-Idiots",
        "language": "Hindi",
        "duration": "2h 28m",
        "price": 220
    },
    {
        "id": 103,
        "movie_name": "Chennai Express",
        "language": "Hindi",
        "duration": "2h 42m",
        "price": 300
    }
])
def test_add_movie(movie):
    try:
        r = requests.post(f"{BASE}/api/movies", json=movie)
        assert r.status_code == 201
    except Exception:
        assert False


def test_get_movie():
    try:
        r = requests.get(f"{BASE}/api/movies/102")
        assert r.status_code == 200
    except Exception:
        assert False


def test_update_movie():
    try:
        r = requests.put(f"{BASE}/api/movies/102", json={"price": 300})
        assert r.status_code == 200
    except Exception:
        assert False

def test_delete_movie():
    try:
        r2 = requests.delete(f"{BASE}/api/movies/103")
        assert r2.status_code == 200
    except Exception:
        assert False


def test_booking(setup_movie):
    data = {
        "movie_id": 101,
        "customer_name": "Sana",
        "tickets": 2
    }

    try:
        r = requests.post(f"{BASE}/api/bookings", json=data)
        assert r.status_code == 201
        assert r.json()["total"] == 500
    except Exception:
        assert False


@pytest.mark.parametrize("data,code", [
    ({"movie_id": 999, "customer_name": "Rahul", "tickets": 1}, 404),
    ({"movie_id": 101, "customer_name": "Rashmi", "tickets": 0}, 400)
])
def test_invalid_booking(data, code):
    try:
        r = requests.post(f"{BASE}/api/bookings", json=data)
        assert r.status_code == code
    except Exception:
        assert False
