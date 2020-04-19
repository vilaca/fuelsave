from app.api import key_service


def test_encode_key(test_app):
    key = key_service.encode_key(data={"username": "username"})
    assert len(key) > 1


def test_decode_key(test_app):
    test = "2test"
    key = key_service.encode_key(data={"username": test})
    print(key)
    assert test == key_service.decode_key(key)


def test_decode_key_fail(test_app):
    test = "2test"
    key = key_service.encode_key(data={"username": ""})
    assert not test == key_service.decode_key(key)
