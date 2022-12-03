#!/bin/env python
import requests

url = "http://localhost:5000/infer"

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

json = {
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


response = requests.post(
    url,
    headers=headers,
    json=json,
)

# response.raise_for_status()
print(response.json())
