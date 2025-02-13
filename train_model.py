# Script to train machine learning model.
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from src.ml.data import process_data
from src.ml.model import compute_metrics_on_slices
from src.ml.model import compute_model_metrics
from src.ml.model import inference
from src.ml.model import save_model
from src.ml.model import train_model


def main():
    data_filename = "census.csv"
    data_dir = "data"
    data_filepath = Path(data_dir, data_filename)
    data = pd.read_csv(data_filepath)

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

    X_test, y_test, _, _ = process_data(
        test,
        categorical_features=cat_features,
        label="salary",
        training=False,
        encoder=encoder,
        lb=lb,
    )

    model = train_model(X_train, y_train)

    save_model(model, encoder, lb)

    y_pred = inference(model, X_test)

    precision, recall, fbeta = compute_model_metrics(y_test, y_pred)

    category_dict = compute_metrics_on_slices(test, model, encoder, lb, cat_features)

    with open("slice_output.txt", "w") as f:
        f.write("All data set metrics\n")
        f.write("precision,recall,fbeta\n")
        f.write(f"{round(precision,3)},{round(recall,3)},{round(fbeta,3)}\n")

        for cat_name, slice_dict in category_dict.items():
            f.write(f"\nMetrics for category: {cat_name}\n")
            f.write("slice_value,precision,recall,fbeta\n")
            for slice_value, metrics in slice_dict.items():
                f.write(
                    f"{slice_value},{round(metrics.precision,3)},{round(metrics.recall,3)},{round(metrics.fbeta,3)}\n"
                )


if __name__ == "__main__":
    main()
