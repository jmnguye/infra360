def test_get_representation_of_client(client):
    response = client.get("/domains/1")
    ref = {"id": 1, "label": "Compute", "value": "Compute"}
    assert response.json == ref
