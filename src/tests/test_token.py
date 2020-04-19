import json
from app.api import crud


def test_create_token_no_body(test_app):
    response = test_app.post("/token")
    assert response.status_code == 422


def test_create_token_no_username(test_app):
    response = test_app.post("/token", data=json.dumps({"username": "user1"}))
    assert response.status_code == 422


def test_create_token_no_password(test_app):
    response = test_app.post("/token", data=json.dumps({"password": "pass1"}))
    assert response.status_code == 422


def test_create_token_wrong_credentials(test_app, monkeypatch):
    async def mock_get(user, passw):
        return None

    monkeypatch.setattr(crud, "get_user", mock_get)

    response = test_app.post(
        "/token", data=json.dumps({"username": "user1", "password": "pass1"})
    )
    assert response.status_code == 401


def test_create_token(test_app, monkeypatch):
    test_data = {"id": 1, "usernanme": "user1", "password": "pass1"}

    async def mock_get(user, passw):
        return test_data

    monkeypatch.setattr(crud, "get_user", mock_get)

    response = test_app.post(
        "/token", data=json.dumps({"username": "user1", "password": "pass1"})
    )
    assert response.status_code == 201
