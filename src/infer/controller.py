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
from src.ml.data import process_data
from src.ml.model import inference

from .enum import Salary


def infer_salary(infer_request: InferRequest) -> InferResponse:
    """Make inference on requested data"""
    df = _create_df_from_infer_request(infer_request)
    model, encoder, lb = _load_model()

    cat_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]

    X, _, _, _ = process_data(
        df,
        categorical_features=cat_features,
        training=False,
        encoder=encoder,
        lb=lb,
    )

    y = inference(model, X)

    def inference_to_salary(y) -> Salary:
        if y not in (0, 1):
            raise InvalidValueError(y, Salary)

        if y == 0:
            return Salary.LEQ_50K

        return Salary.GT_50K

    salary = inference_to_salary(y)

    return InferResponse(salary=salary)


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

    df = pd.DataFrame([infer_dict])[column_order]
    df.rename(columns={col: col.replace("_", "-") for col in column_order}, inplace=True)

    return df
