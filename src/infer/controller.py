"""Module describe infer's controller"""
import pickle
from enum import Enum
from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import OneHotEncoder
from src.infer.model import InferRequest
from src.infer.model import InferResponse


def infer_salary(infer_request: InferRequest) -> InferResponse:
    """Make inference on requested data"""
    df = _create_df_from_infer_request(infer_request)
    model, encoder, lb = _load_model()

    import IPython

    IPython.embed()
    exit(1)

    pass


def _load_model() -> (RandomForestClassifier, OneHotEncoder, LabelBinarizer):
    """Load Random Forest Classifier model, One Hot encoder, and Label Binarizer"""
    model_dir = "model"

    model_filename = "model.pkl"
    encoder_filename = "encoder.pkl"
    lb_filename = "label_binarizer.pkl"

    model = _unpickle(model_dir, model_filename)
    encoder = _unpickle(model_dir, encoder_filename)
    lb = _unpickle(model_dir, lb_filename)

    return model, encoder, lb


def _unpickle(directory, filename):
    """Unpickle data, given directory and filename"""
    with open(Path(directory, filename), "rb") as fd:
        data = pickle.load(fd)
    return data


def _create_df_from_infer_request(infer_request: InferRequest) -> pd.DataFrame:
    """Create pd.DataFrame from InferRequest"""

    def extract_value(e) -> str | int:
        return e.value if isinstance(e, Enum) else e

    infer_dict = {}

    for k, v in infer_request:
        infer_dict[k] = extract_value(v)

    column_order = [
        "age",
        "workclass",
        "fnlgt",
        "education",
        "education_num",
        "marital_status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "capital_gain",
        "capital_loss",
        "hours_per_week",
        "native_country",
    ]

    return pd.DataFrame([infer_dict])[column_order]
