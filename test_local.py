"""Basic API testing on FastAPI."""
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    """Test if root is returning the expected greeting."""
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"greeting": "Hello World!"}
