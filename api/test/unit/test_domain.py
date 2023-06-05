def test_get_representation_of_client(client):
    response = client.get("/domains/1")
    ref = {"id": 1, "label": "Compute", "value": "Compute"}
    assert response.json == ref


def test_update_all_value_of_a_domain(client):
    response = client.put(
        "/domains/1", json={"label": "Compute resource", "value": "Compute"}
    )
    assert response.json == {"id": 1, "label": "Compute resource", "value": "Compute"}
    response = client.get("/domains/1")
    assert response.json == {"id": 1, "label": "Compute resource", "value": "Compute"}


def test_missing_id(client):
    response = client.get("/domains/666")
    assert response.status_code == 404
    assert "domain id not found" in response.json.get("message")


def test_delete_id(client):
    response = client.delete("/domains/1")
    assert response.status_code == 200
    response = client.get("/domains/1")
    assert "domain id not found" in response.json.get("message")


# def test_delete_missing_id(client):
