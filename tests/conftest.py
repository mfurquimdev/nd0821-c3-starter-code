"""Basic configuration for testing FastAPI"""
import pickle
from collections import namedtuple
from pathlib import Path

import dvc.api
import IPython
import numpy as np
import pandas as pd
from dvc.api import DVCFileSystem
from fastapi.testclient import TestClient
from main import app
from pytest import fixture

test_dir = "tests"
data_dir = "data"


@fixture(scope="function")
def client():
    """Return test client for FastAPI"""
    with TestClient(app) as client:
        yield client


@fixture(scope="class")
def X_train():
    """Return X_train"""
    filename = "X_train.csv"
    filepath = Path(test_dir, data_dir, filename)
    return np.loadtxt(filepath, delimiter=",")


@fixture(scope="class")
def y_train():
    """Return y_train"""
    filename = "y_train.csv"
    filepath = Path(test_dir, data_dir, filename)
    return np.loadtxt(filepath, delimiter=",")


@fixture(scope="class")
def X_test():
    """Return X_test"""
    filename = "X_test.csv"
    filepath = Path(test_dir, data_dir, filename)
    return np.loadtxt(filepath, delimiter=",")


@fixture(scope="class")
def y_test():
    """Return y_test"""
    filename = "y_test.csv"
    filepath = Path(test_dir, data_dir, filename)
    return np.loadtxt(filepath, delimiter=",")


@fixture(scope="class")
def y_pred():
    """Return y_pred"""
    filename = "y_pred.csv"
    filepath = Path(test_dir, data_dir, filename)
    return np.loadtxt(filepath, delimiter=",")


@fixture(scope="session")
def model():
    """Return model"""
    print("\nRetrieving model from s3 for test purposes")
    url = "https://github.com/mfurquimdev/nd0821-c3-starter-code"

    data = dvc.api.read("model/model.pkl", repo=url, mode="rb")
    model = pickle.loads(data)
    print("Model retrieved")

    return model


@fixture(scope="session")
def encoder():
    """Return encoder"""
    print("\nRetrieving encoder from s3 for test purposes")
    url = "https://github.com/mfurquimdev/nd0821-c3-starter-code"

    data = dvc.api.read("model/encoder.pkl", repo=url, mode="rb")
    encoder = pickle.loads(data)
    print("Encoder retrieved")

    return encoder


@fixture(scope="session")
def lb():
    """Return encoder"""
    print("\nRetrieving label binarizer from s3 for test purposes")
    url = "https://github.com/mfurquimdev/nd0821-c3-starter-code"

    data = dvc.api.read("model/label_binarizer.pkl", repo=url, mode="rb")
    lb = pickle.loads(data)
    print("Label binarizer retrieved")

    return lb


@fixture(scope="session")
def data():
    """Return CSV data"""
    print("\nRetrieving csv data from s3 for test purposes")
    url = "https://github.com/mfurquimdev/nd0821-c3-starter-code"

    with dvc.api.open("data/census.csv", repo=url) as f:
        data = pd.read_csv(f)

    print("Data retrieved")

    return data


@fixture(scope="session")
def cat_features():
    """Categorical Features"""
    return [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]


@fixture(scope="session")
def num_features():
    """Numerical Features tuple"""
    num_feat = namedtuple("NumericalFeature", ["name", "min", "max"])

    return [
        num_feat("hours-per-week", 28, 53),
        num_feat("age", 20, 59),
        num_feat("fnlgt", 27882, 295329),
        num_feat("education-num", 1, 16),
    ]
