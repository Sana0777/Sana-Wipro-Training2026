import pytest
import requests
from bs4 import BeautifulSoup

BASE = "http://127.0.0.1:5000"


@pytest.fixture(scope="session")
def base_url():
    return BASE


@pytest.mark.parametrize("patient", [
    {"name": "Rama", "age": 23, "gender": "Male", "contact": "12345", "disease": "Flu", "doctor": "Dr. Narula"},
    {"name": "Rani", "age": 24, "gender": "Female", "contact": "76543", "disease": "Cold", "doctor": "Dr. Saksena"}
])
def test_add_patient(base_url, patient):
    r = requests.post(f"{base_url}/api/patients", json=patient)
    assert r.status_code == 201


def test_get_patients(base_url):
    r = requests.get(f"{base_url}/api/patients")
    assert r.status_code == 200
    assert isinstance(r.json(), list)


@pytest.mark.xfail
def test_invalid_get(base_url):
    r = requests.get(f"{base_url}/api/patients/999")
    assert r.status_code == 200


@pytest.mark.skip(reason="Demo skip")
def test_skip_example():
    assert True


def test_scrape_patients():
    r = requests.get("http://127.0.0.1:5000/patients")
    soup = BeautifulSoup(r.text, "html.parser")

    rows = soup.find_all("tr")[1:]

    for row in rows:
        cols = row.find_all("td")

        name = cols[0].text.strip()
        age = cols[1].text.strip()
        disease = cols[2].text.strip()
        doctor = cols[3].text.strip()

        assert name
        assert age
        assert disease
        assert doctor

def test_delete_patient_by_id(base_url):
    pid = 1
    r = requests.delete(f"{base_url}/api/patients/{pid}")
    assert r.status_code == 200
    check = requests.get(f"{base_url}/api/patients/{pid}")
    assert check.status_code == 404

