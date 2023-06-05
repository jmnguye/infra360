def test_get_domains(client):
    response = client.get("/domains")
    assert b"Compute" in response.data
    assert b"Network" in response.data
    assert b"Storage" in response.data


def test_add_a_domain(client):
    client.post("/domains", json={"label": "Dummy", "value": "Dummy"})
    response = client.get("/domains")
    assert b"Compute" in response.data
    assert b"Network" in response.data
    assert b"Storage" in response.data
    assert b"Dummy" in response.data


def test_add_misformed_payload(client):
    response = client.post("/domains", json={"label": 1234, "val": "Dummy"})
    assert b"Input payload validation failed" in response.data


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
