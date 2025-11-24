import pandas as pd
import os

RAW_DIR = "data/raw"
OUTPUT_DIR = "data/processed"

TRANSACTION_FILE = os.path.join(RAW_DIR, "train_transaction.csv")
IDENTITY_FILE = os.path.join(RAW_DIR, "train_identity.csv")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "train_merged_clean.csv")

print("[INFO] Loading raw data...")

train_transaction = pd.read_csv(TRANSACTION_FILE)
train_identity = pd.read_csv(IDENTITY_FILE)

print("[INFO] Merging datasets...")
train = train_transaction.merge(train_identity, on="TransactionID", how="left")

print("[INFO] Cleaning data...")
train = train.fillna(-1)

os.makedirs(OUTPUT_DIR, exist_ok=True)
train.to_csv(OUTPUT_FILE, index=False)

print(f"[INFO] Saved cleaned merged file to {OUTPUT_FILE}")
