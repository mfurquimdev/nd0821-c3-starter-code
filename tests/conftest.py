"""Basic configuration for testing FastAPI"""
from pathlib import Path

import numpy as np
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
def y_infer():
    """Return y_pred"""
    filename = "y_pred.csv"
    filepath = Path(test_dir, data_dir, filename)
    return np.loadtxt(filepath, delimiter=",")


@fixture(scope="class")
def model():
    """Return y_pred"""
    from dvc.api import DVCFileSystem

    model_dir = Path("test", "model")
    fs = DVCFileSystem(model_dir)
    import IPython

    IPython.embed()
    exit(1)

    filename = "y_pred.csv"
    filepath = Path(test_dir, data_dir, filename)
    return np.loadtxt(filepath, delimiter=",")
