from app.api import vehicles, crud, key_service


def test_no_login(test_app):
    response = test_app.get("/vehicles")
    assert response.status_code == 401


def test_get_vehicle_list(test_app, monkeypatch):
    test_data = [{"id": 1, "owner": "user1", "distance": 34}]
    test_data2 = key_service.encode_key(data={"username": "user1"})

    async def mock_list(user):
        return test_data

    async def mock_get_api_key(user):
        return test_data

    monkeypatch.setattr(crud, "get_vehicles", mock_list)
    monkeypatch.setattr(vehicles, "get_api_key", mock_get_api_key)

    response = test_app.get("/vehicles?api-key=" + test_data2)
    assert response.status_code == 200


def test_get_vehicle_list_w_header(test_app, monkeypatch):
    test_data = [{"id": 1, "owner": "user1", "distance": 34}]
    test_data2 = key_service.encode_key(data={"username": "user1"})

    async def mock_list(user):
        return test_data

    async def mock_get_api_key(user):
        return test_data

    monkeypatch.setattr(crud, "get_vehicles", mock_list)
    monkeypatch.setattr(vehicles, "get_api_key", mock_get_api_key)

    response = test_app.get(
        "/vehicles", headers={"Authorization": "Bearer " + test_data2}
    )
    assert response.status_code == 200


def test_get_vehicle_list_bad_api_key(test_app, monkeypatch):
    test_data = [{"id": 1, "owner": "user1", "distance": 34}]
    test_data2 = "bad-api-key-:("

    async def mock_list(user):
        return test_data

    async def mock_get_api_key(user):
        return test_data

    monkeypatch.setattr(crud, "get_vehicles", mock_list)
    monkeypatch.setattr(vehicles, "get_api_key", mock_get_api_key)

    response = test_app.get("/vehicles?api-key=" + test_data2)
    assert response.status_code == 401
