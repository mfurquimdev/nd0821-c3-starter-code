"""Basic API testing on FastAPI."""


def test_root(client):
    """Test if root is returning the expected greeting."""
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"greeting": "Bye World!"}
