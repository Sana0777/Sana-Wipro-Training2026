import csv
import os
import logging

logger = logging.getLogger(__name__)

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")


def read_csv(filename):
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Test data file not found: {path}\n"
            f"Expected location: {DATA_DIR}"
        )
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    logger.info(f"Loaded {len(rows)} row(s) from {path}")
    return rows


def load_data():

    rows = read_csv("test_data.csv")
    return [
        (
            r["first_name"],
            r["last_name"],
            r["email"],
            r["password"],
            r["gender"],
            r["product_search"],
            r["product_name"],
            int(r["add_quantity"]),
            int(r["updated_quantity"]),
        )
        for r in rows
    ]
