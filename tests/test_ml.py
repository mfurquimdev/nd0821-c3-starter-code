"""Write at least 3 unit tests. Unit testing ML can be hard due to the stochasticity
-- at least test if any ML functions return the expected type."""
from sklearn.ensemble import RandomForestClassifier
from src.ml.model import compute_model_metrics
from src.ml.model import inference
from src.ml.model import train_model


# class TestTrainModel:
#     def test_train_model(self, X_train, y_train):
#         """Test train model returns correct model type"""
#         model = train_model(X_train, y_train)
#         assert isinstance(model, RandomForestClassifier)


class TestInference:
    def test_inference(self, model, X_test):
        pass


# class TestComputeModelMetrics:
#     def test_compute_model_metrics(self, y_test, y_pred):
#         precision, recall, fbeta = compute_model_metrics(y_test, y_pred)
