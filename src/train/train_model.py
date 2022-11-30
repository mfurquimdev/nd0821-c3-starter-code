# Script to train machine learning model.
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from src.ml.data import process_data
from src.ml.model import compute_model_metrics
from src.ml.model import inference
from src.ml.model import save_model
from src.ml.model import train_model

# Add the necessary imports for the starter code.

# Add code to load in the data.
data_filename = "census.csv"
data_dir = "data"
data_filepath = Path(data_dir, data_filename)
data = pd.read_csv(data_filepath)

test_dir = "tests"
data_dir = "data"


n = 5

# Optional enhancement, use K-fold cross validation instead of a train-test split.
train, test = train_test_split(data, test_size=0.20)

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

X_train, y_train, encoder, lb = process_data(
    train,
    categorical_features=cat_features,
    label="salary",
    training=True,
)

filename = "X_train.csv"
filepath = Path(test_dir, data_dir, filename)
np.savetxt(filepath, X_train[:n], delimiter=",")

filename = "y_train.csv"
filepath = Path(test_dir, data_dir, filename)
np.savetxt(filepath, y_train[:n], delimiter=",")

# Proces the test data with the process_data function.
X_test, y_test, _, _ = process_data(
    test,
    categorical_features=cat_features,
    label="salary",
    training=False,
    encoder=encoder,
    lb=lb,
)

filename = "X_test.csv"
filepath = Path(test_dir, data_dir, filename)
np.savetxt(filepath, X_test[:n], delimiter=",")

filename = "y_test.csv"
filepath = Path(test_dir, data_dir, filename)
np.savetxt(filepath, y_test[:n], delimiter=",")

# Train and save a model.
model = train_model(X_train, y_train)

save_model(model, encoder, lb)

y_pred = inference(model, X_test)

filename = "y_pred.csv"
filepath = Path(test_dir, data_dir, filename)
np.savetxt(filepath, y_pred[-n:], delimiter=",")

precision, recall, fbeta = compute_model_metrics(y_test, y_pred)
print(f"precision: {precision}")
print(f"recall: {recall}")
print(f"fbeta: {fbeta}")
