LLM Fraud Detection Assistant

A hybrid fraud detection system that combines machine learning models, engineered fraud rules, and a Large Language Model (LLM) to detect and explain suspicious financial transactions. Inspired by real-world banking systems used by Capital One, Chase, Wells Fargo, and AmEx.

Project Overview

Financial fraud is becoming more sophisticated due to account takeovers, device spoofing, identity theft, velocity attacks, and cross-border risks. Traditional ML models often lack transparency, while rules alone are too limited.

This project provides an LLM-powered Fraud Detection Assistant that can:

Score transactions using trained ML models

Detect fraud patterns using bank-style rule checks

Generate human-like explanations with an LLM

Provide a simple analyst review dashboard

The goal is to create an interpretable, transparent, and industry-aligned fraud detection workflow.

Key Features

Hybrid Risk Engine: ML model + rule engine + LLM reasoning

Analyst Dashboard: Enter transactions and view fraud insights

Machine Learning: Logistic Regression, Random Forest, LightGBM

Fraud Rules Implemented:

High amount

Very small amount

Suspicious ranges

Threshold-avoidance behavior

Repeated digit patterns

Rounded amounts

Explainable AI: Natural-language explanations for analysts

Dataset: IEEE-CIS Fraud Detection (1M+ transactions)

Dataset: IEEE-CIS Fraud Detection

The project uses the public Kaggle dataset:

train_transaction.csv — transaction-level data

train_identity.csv — device & browser metadata

test_transaction.csv — test set

test_identity.csv — identity metadata

⚠️ Dataset files are NOT included in this repo due to size and licensing.
Download them from Kaggle and place them in:


---

llm-fraud-detection-assistant/
│
├── data/
│   ├── raw/                # Raw Kaggle data (not uploaded)
│   ├── processed/          # Cleaned & merged datasets
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│
├── app/
│   ├── __init__.py
│   ├── main.py             # Flask app entry point
│   ├── rules_engine.py     # Bank-style fraud rules
│   ├── llm_explainer.py    # LLM prompts + explanations
│   ├── models.py           # ML model loading + scoring
│
├── models/
│   ├── fraud_model.pkl     # Trained ML model
│   ├── scaler.pkl
│
├── scripts/
│   ├── prepare_data.py
│   ├── train_model.py
│
├── docs/
│   ├── screenshot_homepage.png
│   ├── screenshot_result.png
│
├── .gitignore
├── requirements.txt
├── README.md

```
Initial working version of the LLM Fraud Detection Assistant.

Completed Today

Project folder structure created

Added Flask backend (app/main.py)

Implemented UI with Bootstrap

Added fraud rules (HighAmount, VerySmallAmount, etc.)

Built placeholder ML fraud scoring logic

Added LLM reasoning module (fallback explanation)

Added CSS + HTML template structure

App tested successfully at:
http://127.0.0.1:5000

Screenshot

Home Page Screenshot
![Home Page](docs/screenshot_homepage.png)

Fraud Result Screenshot
![Fraud Result](docs/screenshot_result.png)

Model & Training (Added November 24, 2025)

Today, I implemented and trained the project’s first machine learning fraud model, connected it to the Flask app, and prepared the full ML pipeline.

✔ Data Preparation

Using the IEEE-CIS dataset, I:

Loaded raw transaction + identity data

Merged and cleaned both tables

Saved the processed dataset to:
data/processed/train_merged_clean.csv

✔ Model Training

Trained a baseline Logistic Regression model:

Scaled numerical features

Trained/validated using a simple split

Achieved 96.5% validation accuracy

Saved artifacts to:

models/fraud_model.pkl

models/scaler.pkl

✔ App Integration

The trained model is now integrated directly into the Flask app:

Loads automatically at startup

Generates a fraud probability score for each transaction

Works together with the rules engine

Provides consistent and predictable results

This completes the first full version of the ML pipeline, making the project functional end-to-end.

  screenshot
##  Model Output Examples updated

These screenshots show how the fraud rules + ML model respond to different types of transactions.

---

###  Very Small Amount — Rule Triggered
![Very Small Amount](docs/screenshot_very_small_amount.png)

---

### High Amount + Pattern Rules Triggered
![High Amount](docs/screenshot_high_amount.png)

---

###  Normal Transaction — No Rules Triggered
![No Rules](docs/screenshot_no_rules.png)
