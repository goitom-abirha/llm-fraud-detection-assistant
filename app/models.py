import os
import numpy as np
import joblib

DEFAULT_MODEL_PATH = os.getenv("MODEL_PATH", "models/fraud_model.pkl")
DEFAULT_SCALER_PATH = os.getenv("SCALER_PATH", "models/scaler.pkl")

def load_model(model_path: str = DEFAULT_MODEL_PATH,
               scaler_path: str = DEFAULT_SCALER_PATH):
    """
    Load trained ML model and scaler.
    If they don't exist yet, return (None, None) so the app can still run.
    """
    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        print("[INFO] Model or scaler not found. Run train_model.py first.")
        return None, None

    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    print("[INFO] Model and scaler loaded.")
    return model, scaler


def score_transaction(transaction: dict, model, scaler):
    """
    Take a raw transaction dict and return a fraud score 0–1.

    For now, only 'TransactionAmt' is used.
    """
    if model is None or scaler is None:
        return None

    amount = float(transaction.get("TransactionAmt", 0.0))
    X = np.array([[amount]])
    X_scaled = scaler.transform(X)

    return model.predict_proba(X_scaled)[0, 1]
