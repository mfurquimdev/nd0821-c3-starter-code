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

        expected_output = np.array([0, 0])
        assert np.array_equal(y_pred, expected_output)


class TestComputeModelMetrics:
    """Test metrics computation"""

    def test_compute_model_metrics(self, y_test, y_pred):
        """Test metrics computation from previously calculated y_pred"""
        precision, recall, fbeta = compute_model_metrics(y_test, y_pred)
        assert isinstance(precision, float)
        assert isinstance(recall, float)
        assert isinstance(fbeta, float)

        assert precision == 0.5
        assert recall == 1
        assert round(fbeta, 3) == 0.667
