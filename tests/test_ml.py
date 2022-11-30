"""Write at least 3 unit tests. Unit testing ML can be hard due to the stochasticity
-- at least test if any ML functions return the expected type."""
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from src.ml.model import compute_model_metrics
from src.ml.model import inference
from src.ml.model import train_model


class TestTrainModel:
    """Test train model"""

    def test_train_model(self, X_train, y_train):
        """Test train model returns correct model type"""
        model = train_model(X_train, y_train)
        assert isinstance(model, RandomForestClassifier)


class TestInference:
    """Test inference"""

    def test_inference(self, model, X_test):
        """Test inference with model and X_test data"""
        y_pred = inference(model, X_test)
        assert isinstance(y_pred, np.ndarray)

        expected_output = np.array([0, 0, 0, 1, 0])
        assert np.array_equal(y_pred, expected_output)


class TestComputeModelMetrics:
    """Test metrics computation"""

    def test_compute_model_metrics(self, y_test, y_pred):
        """Test metrics computation from previously calculated y_pred"""
        precision, recall, fbeta = compute_model_metrics(y_test, y_pred)
        assert isinstance(precision, float)
        assert isinstance(recall, float)
        assert isinstance(fbeta, float)

        assert precision == 1
        assert round(recall, 3) == 0.333
        assert round(fbeta, 3) == 0.5


# class TestSliceValidation:
#     def test_data_shape(self, data):
#         """If your data is assumed to have no null values then this is a valid test."""
#         assert data.shape == data.dropna().shape, "Dropping null changes shape."

#     def test_slice_averages(self, data, cat_features):
#         """Test to see if our mean per categorical slice is in the range 1.5 to 2.5."""
#         numeric_feat = set(data.columns) - set(cat_features)
#         for cat_feat in data[cat_features].unique():
#             avg_value = data[data[cat_features] == cat_feat][numeric_feat].mean()
#             assert 2.5 > avg_value > 1.5, f"For {cat_feat}, average of {avg_value} not between 2.5 and 3.5."
