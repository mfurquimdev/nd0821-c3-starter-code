"""Basic configuration for testing FastAPI"""
import pickle
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


@fixture(scope="module")
def model():
    """Return model"""

    print("\nRetrieving model from github for test purposes")
    url = "https://github.com/mfurquimdev/nd0821-c3-starter-code"

    data = dvc.api.read("model/model.pkl", repo=url, mode="rb")
    model = pickle.loads(data)
    print("Model retrieved")

    return model


@fixture(scope="module")
def data():
    """Return CSV data"""
    data_filename = "census.csv"
    data_dir = "data"
    data_filepath = Path(data_dir, data_filename)
    return pd.read_csv(data_filepath)


@fixture(scope="module")
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
