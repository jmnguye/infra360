import pytest


def test_get_domains(client):
    response = client.get("/domains")
    assert b"Compute" in response.data
    assert b"Network" in response.data
    assert b"Storage" in response.data
