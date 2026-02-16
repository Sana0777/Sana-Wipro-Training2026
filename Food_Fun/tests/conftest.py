import pytest
from flask import Flask
from routes.users import user_bp
from routes.restaurants import restaurant_bp
from routes.dishes import dish_bp
from routes.orders import order_bp
from routes.ratings import rating_bp
from routes.admin import admin_bp
from config import (users, restaurants, dishes, orders, ratings, feedbacks)
import config

@pytest.fixture
def app():
    app = Flask(__name__)

    app.register_blueprint(user_bp)
    app.register_blueprint(restaurant_bp)
    app.register_blueprint(dish_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(rating_bp)
    app.register_blueprint(admin_bp)

    app.config["TESTING"] = True
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture(autouse=True)
def reset_memory_and_counters():

    users.clear()
    restaurants.clear()
    dishes.clear()
    orders.clear()
    ratings.clear()
    feedbacks.clear()


    config.user_counter = 0
    config.restaurant_counter = 0
    config.order_counter = 0
    config.dish_counter = 0
    config.rating_counter = 0
