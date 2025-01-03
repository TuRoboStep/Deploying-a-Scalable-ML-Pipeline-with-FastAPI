from pathlib import Path
import pytest
from sklearn.ensemble import RandomForestClassifier
from ml.data import apply_label
from ml.model import compute_model_metrics, save_model
import numpy as np

def test_model_metrics():
    """
    # Test model metrics for precision, recall, and F1.
    """
    y = np.array([1, 1, 1, 0, 0, 0])
    preds = np.array([1, 1, 0, 0, 0, 1])
    p, r, f1 = compute_model_metrics(y, preds)

    assert p == 2/3
    assert r == 2/3
    assert f1 == 2/(1/p+1/r)


# TODO: implement the second test. Change the function name and input as needed
def test_save_model(tmp_path):
    """
    # Tests if the save model function actually saves a model
    """
    # save model to tmp directory
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model_path = Path(tmp_path) / 'model.pkl'
    save_model(model, model_path)
    assert model_path.exists()


def test_apply_label():
    """
    # Test if the apply label function actually returns the correct string.
    """
    assert apply_label([1]) == ">50K"
    assert apply_label([0]) == "<=50K"
