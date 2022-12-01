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

    def test_infer_post_wrong_education(self, client):
        """Test if root is returning the expected greeting."""
        data = {
            "age": 17,
            "education": "4th-6th",
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

        assert r.status_code == 422

        wrong_education_response = {
            "detail": [
                {
                    "loc": ["body", "education"],
                    "msg": (
                        "value is not a valid enumeration member; "
                        "permitted: 'Assoc-acdm', 'Assoc-voc', 'Bachelors', 'Doctorate', 'HS-grad', 'Masters', "
                        "'10th', '11th', '12th', '1st-4th', '5th-6th', '7th-8th', '9TH', 'Preschool', "
                        "'Prof-school', 'Some-college'"
                    ),
                    "type": "type_error.enum",
                    "ctx": {
                        "enum_values": [
                            "Assoc-acdm",
                            "Assoc-voc",
                            "Bachelors",
                            "Doctorate",
                            "HS-grad",
                            "Masters",
                            "10th",
                            "11th",
                            "12th",
                            "1st-4th",
                            "5th-6th",
                            "7th-8th",
                            "9TH",
                            "Preschool",
                            "Prof-school",
                            "Some-college",
                        ]
                    },
                }
            ]
        }
        assert r.json() == wrong_education_response

    def test_infer_post_missing_age(self, client):
        """Test if root is returning the expected greeting."""
        data = {
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

        assert r.status_code == 422

        missing_age_response = {
            "detail": [
                {
                    "loc": ["body", "age"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
            ]
        }
        assert r.json() == missing_age_response

    def test_infer_post_negative_age(self, client):
        """Test if root is returning the expected greeting."""
        data = {
            "age": -1,
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

        assert r.status_code == 422

        nagative_age_response = {
            "detail": [
                {
                    "ctx": {"limit_value": 0},
                    "loc": ["body", "age"],
                    "msg": "ensure this value is greater than 0",
                    "type": "value_error.number.not_gt",
                }
            ]
        }
        assert r.json() == nagative_age_response

    def test_infer_post_high_age(self, client):
        """Test if root is returning the expected greeting."""
        data = {
            "age": 151,
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

        assert r.status_code == 422

        nagative_age_response = {
            "detail": [
                {
                    "ctx": {"limit_value": 150},
                    "loc": ["body", "age"],
                    "msg": "ensure this value is less than 150",
                    "type": "value_error.number.not_lt",
                }
            ]
        }
        assert r.json() == nagative_age_response

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
