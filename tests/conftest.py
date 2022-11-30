"""Basic configuration for testing FastAPI"""
from pathlib import Path

import dvc.api
import joblib
import numpy as np
import pandas as pd
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
    with dvc.api.open(
        repo="https://github.com/mfurquimdev/nd0821-c3-starter-code",
        path="model/model.sav",
        rev="model",
        mode="rb",
    ) as fd:
        model = joblib.load(fd)

    print("Model retrieved")

    return model
