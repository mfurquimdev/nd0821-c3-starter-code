"""Basic configuration for testing FastAPI"""
from fastapi.testclient import TestClient
from pytest import fixture

from main import app


@fixture(scope="function")
def client():
    """Return test client for FastAPI"""
    with TestClient(app) as client:
        yield client
