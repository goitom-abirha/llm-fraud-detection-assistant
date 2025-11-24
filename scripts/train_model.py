import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

DATA_FILE = "data/processed/train_merged_clean.csv"
MODEL_PATH = "models/fraud_model.pkl"
SCALER_PATH = "models/scaler.pkl"

print("[INFO] Loading processed data...")
df = pd.read_csv(DATA_FILE)

# Simple version: only TransactionAmt as feature
X = df[["TransactionAmt"]].values
y = df["isFraud"].values

X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("[INFO] Scaling features...")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)

print("[INFO] Training Logistic Regression model...")
model = LogisticRegression(max_iter=200)
model.fit(X_train_scaled, y_train)

accuracy = model.score(X_val_scaled, y_val)
print(f"[INFO] Validation accuracy: {accuracy:.4f}")

os.makedirs("models", exist_ok=True)
joblib.dump(model, MODEL_PATH)
joblib.dump(scaler, SCALER_PATH)

print(f"[INFO] Saved model to {MODEL_PATH}")
print(f"[INFO] Saved scaler to {SCALER_PATH}")
