from app.api import token_service


def test_create_token_no_body(test_app):
    key = token_service.create_token(data={"username": "username"})
    assert len(key) > 1
