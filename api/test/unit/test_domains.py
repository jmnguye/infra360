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
