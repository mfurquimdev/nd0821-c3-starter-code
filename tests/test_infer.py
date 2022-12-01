"""Test /infer endpoint."""


class TestInfer:
    """Test /infer endpoint"""

    def test_infer_post_success(self, client):
        """Test if root is returning the expected greeting."""
        data = {
            "age": 17,
            "education": "5th-6th",
            "capital_gain": 1077.64,
            "capital_loss": 87.30,
            "education_num": 10,
            "fnlgt": 189778.40,
            "hours_per_week": 40,
            "marital_status": "Married-civ-spouse",
            "native_country": "Canada",
            "occupation": "Farming-fishing",
            "race": "White",
            "relationship": "Own-child",
            "sex": "Male",
            "workclass": "Self-emp-inc",
        }
        r = client.post("/infer", json=data)

        assert r.status_code == 200

        assert r.json() == {"salary": "<=50K"}

    def test_infer_post_empty_json(self, client):
        """Test if root is returning the expected greeting."""
        data = {}
        r = client.post("/infer", json=data)

        assert r.status_code == 422

        missing_fields_response = {
            "detail": [
                {"loc": ["body", "age"], "msg": "field required", "type": "value_error.missing"},
                {"loc": ["body", "capital_gain"], "msg": "field required", "type": "value_error.missing"},
                {"loc": ["body", "capital_loss"], "msg": "field required", "type": "value_error.missing"},
                {"loc": ["body", "education"], "msg": "field required", "type": "value_error.missing"},
                {"loc": ["body", "education_num"], "msg": "field required", "type": "value_error.missing"},
                {"loc": ["body", "fnlgt"], "msg": "field required", "type": "value_error.missing"},
                {"loc": ["body", "hours_per_week"], "msg": "field required", "type": "value_error.missing"},
                {"loc": ["body", "marital_status"], "msg": "field required", "type": "value_error.missing"},
                {"loc": ["body", "native_country"], "msg": "field required", "type": "value_error.missing"},
                {"loc": ["body", "occupation"], "msg": "field required", "type": "value_error.missing"},
                {"loc": ["body", "race"], "msg": "field required", "type": "value_error.missing"},
                {"loc": ["body", "relationship"], "msg": "field required", "type": "value_error.missing"},
                {"loc": ["body", "sex"], "msg": "field required", "type": "value_error.missing"},
                {"loc": ["body", "workclass"], "msg": "field required", "type": "value_error.missing"},
            ],
        }

        assert r.json() == missing_fields_response

    def test_infer_post_empty_no_data(self, client):
        """Test if root is returning the expected greeting."""
        r = client.post("/infer")
        assert r.status_code == 422
        assert r.json() == {"detail": [{"loc": ["body"], "msg": "field required", "type": "value_error.missing"}]}

    def test_infer_get(self, client):
        """Test if root is returning the expected greeting."""
        r = client.get("/infer")
        assert r.status_code == 405
        assert r.json() == {"detail": "Method Not Allowed"}
