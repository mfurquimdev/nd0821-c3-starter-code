"""Test /infer endpoint."""


class TestInfer:
    """Test /infer endpoint"""

    def test_infer_post_empty_body(self, client):
        """Test if root is returning the expected greeting."""
        r = client.post("/infer")
        assert r.status_code == 422
        assert r.json() == {"detail": [{"loc": ["body"], "msg": "field required", "type": "value_error.missing"}]}

    def test_infer_get(self, client):
        """Test if root is returning the expected greeting."""
        r = client.get("/infer")
        assert r.status_code == 405
        assert r.json() == {"detail": "Method Not Allowed"}
