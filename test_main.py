from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home_page():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == \
        "Password Strength Checker API"


def test_weak_password():

    response = client.post(
        "/check-password",
        json={"password": "abc"}
    )

    assert response.status_code == 200
    assert response.json()["strength"] == "Weak"


def test_medium_password():

    response = client.post(
        "/check-password",
        json={"password": "Password123"}
    )

    assert response.status_code == 200
    assert response.json()["strength"] == "Medium"


def test_strong_password():

    response = client.post(
        "/check-password",
        json={"password": "MySecure@Password2026"}
    )

    assert response.status_code == 200
    assert response.json()["strength"] == "Strong"


def test_real_world_google_style():

    response = client.post(
        "/check-password",
        json={"password": "Google@2026"}
    )

    assert response.status_code == 200
    assert response.json()["strength"] == "Strong"


def test_real_world_bank_password():

    response = client.post(
        "/check-password",
        json={"password": "Banking#Secure2026"}
    )

    assert response.status_code == 200
    assert response.json()["strength"] == "Strong"


def test_empty_password():

    response = client.post(
        "/check-password",
        json={"password": ""}
    )

    assert response.status_code == 400
