"""Module defining model training, metrics computation, and inferece."""
import pickle
from collections import namedtuple
from pathlib import Path

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import fbeta_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from src.ml.data import process_data

# Optional: implement hyperparameter tuning.
def train_model(X_train, y_train):
    """
    Trains a machine learning model and returns it.

    Inputs
    ------
    X_train : np.array
        Training data.
    y_train : np.array
        Labels.

    Returns
    -------
    model
        Trained machine learning model.
    """
    rfc = RandomForestClassifier(max_depth=25, n_estimators=30, max_features=14)

    return rfc.fit(X_train, y_train)


def compute_model_metrics(y, preds):
    """
    Validates the trained machine learning model using precision, recall, and F1.

    Inputs
    ------
    y : np.array
        Known labels, binarized.
    preds : np.array
        Predicted labels, binarized.

    Returns
    -------
    precision : float
    recall : float
    fbeta : float
    """
    fbeta = fbeta_score(y, preds, beta=1, zero_division=1)
    precision = precision_score(y, preds, zero_division=1)
    recall = recall_score(y, preds, zero_division=1)

    return precision, recall, fbeta


def inference(model, X):
    """
    Run model inferences and return the predictions.

    Inputs
    ------
    model : ???
        Trained machine learning model.
    X : np.array
        Data used for prediction.

    Returns
    -------
    preds : np.array
        Predictions from the model.
    """
    return model.predict(X)


def compute_metrics_on_slices(column, data, model, encoder, lb, cat_features):
    slice_dict = {}
    slice_metrics = namedtuple("SliceMetrics", ["precision", "recall", "fbeta"])
    for col_value in data[column].unique():
        X, y, _, _ = process_data(
            data[data[column] == col_value],
            categorical_features=cat_features,
            label="salary",
            training=False,
            encoder=encoder,
            lb=lb,
        )
        y_pred = inference(model, X)

        precision, recall, fbeta = compute_model_metrics(y, y_pred)
        slice_dict[col_value] = slice_metrics(precision, recall, fbeta)

    return slice_dict


def save_model(model, encoder, lb):
    """
    Save model, encoder and label binarizer.

    Inputs
    ------
    model : ???
        Trained machine learning model.
    encoder : sklearn.preprocessing._encoders.OneHotEncoder
        Trained sklearn OneHotEncoder, only used if training=False.
    lb : sklearn.preprocessing._label.LabelBinarizer
        Trained sklearn LabelBinarizer, only used if training=False.

    Returns
    -------
    None
    """
    model_dir = "model"
    Path(model_dir).mkdir(parents=True, exist_ok=True)

    model_filename = "model.pkl"
    model_filepath = Path(model_dir, model_filename)

    encoder_filename = "encoder.pkl"
    encoder_filepath = Path(model_dir, encoder_filename)

    label_binarizer_filename = "label_binarizer.pkl"
    label_binarizer_filepath = Path(model_dir, label_binarizer_filename)

    with open(model_filepath, "wb") as f:
        pickle.dump(model, f)

    with open(encoder_filepath, "wb") as f:
        pickle.dump(encoder, f)

    with open(label_binarizer_filepath, "wb") as f:
        pickle.dump(lb, f)
