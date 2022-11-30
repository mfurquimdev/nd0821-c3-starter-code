"""Basic API testing on FastAPI."""


def test_root(client):
    """Test if root is returning the expected greeting."""
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"greeting": "Hello World!"}


def test_root_fail(client):
    """Test if root fails when query param is True."""
    r = client.get("/?fail=True")
    assert r.status_code == 404
    assert r.json() == {"detail": "Fail flag is True"}
