"""Write at least 3 unit tests. Unit testing ML can be hard due to the stochasticity
-- at least test if any ML functions return the expected type."""
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from src.ml.data import process_data
from src.ml.model import compute_metrics_on_slices
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

    def test_education_metrics(self, data, model, encoder, lb, cat_features):
        """Test metrics for education slice"""
        ed_dict = compute_metrics_on_slices("education", data, model, encoder, lb, cat_features)

        precision_min = 0.88
        recall_min = 0.55
        fbeta_min = 0.70

        for ed_value, metrics in ed_dict.items():
            assert metrics.precision >= precision_min, f"{ed_value} has precision less than {precision_min}"
            assert metrics.recall >= recall_min, f"{ed_value} has recall less than {recall_min}"
            assert metrics.fbeta >= fbeta_min, f"{ed_value} has fbeta less than {fbeta_min}"


class TestData:
    """Test data in shape and value's average in categorical features"""

    def test_data_shape(self, data):
        """If your data is assumed to have no null values then this is a valid test."""
        assert data.shape == data.dropna().shape, "Dropping null changes shape."

    def test_slice_averages(self, data, cat_features, num_features):
        """Test to see if our mean per categorical slice is in the range specified on the fixture."""
        for cat_feat in cat_features:
            for val_feat in data[cat_feat].unique():
                for num_feat, min_val, max_val in num_features:
                    avg_val_feat = data[data[cat_feat] == val_feat][num_feat].mean()

                    assert (
                        min_val <= avg_val_feat <= max_val
                    ), f"For {cat_feat}, {val_feat} average of {avg_val_feat} in {num_feat} not between {min_val} and {max_val}."
