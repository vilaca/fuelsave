from app.api import hashing_service


def test_encode_key(test_app):
    encoded: str = hashing_service.hash("hellokey")
    assert hashing_service.compare("hellokey", encoded)
