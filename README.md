# LLM Fraud Detection Assistant

A hybrid fraud detection system combining **machine learning models**, **engineered fraud rules**, and a **Large Language Model (LLM)** to detect and explain suspicious financial transactions.  
Inspired by real-world fraud workflows used at Capital One, Chase, Wells Fargo, and AmEx.

---

## 🚀 Project Overview

Financial fraud is becoming more sophisticated due to:

- Account takeovers  
- Device spoofing  
- Identity theft  
- Velocity attacks  
- Cross-border risks  

Traditional ML models can be hard to interpret, and rule-based systems alone are too limited.

This project provides an **LLM-powered Fraud Detection Assistant** that can:

- Score transactions using trained ML models  
- Detect fraud signals using bank-style rule checks  
- Generate human-like explanations (LLM fallback version included)  
- Provide a simple web-based analyst dashboard  

The goal is an **interpretable, transparent, industry-aligned fraud detection workflow**.

---

## 🔍 Key Features

- **Hybrid Risk Engine** → ML model + rule engine + LLM reasoning  
- **Analyst Dashboard** → Flask web interface for live scoring  
- **Machine Learning Models**  
  - Logistic Regression (baseline)  
  - Ready for Random Forest / LightGBM upgrades  
- **Fraud Rules Implemented**
  - High Amount  
  - Very Small Amount  
  - Suspicious Ranges  
  - Threshold-Avoidance Attempts  
  - Repeated/Duplicate Digits  
  - Rounded Amount Patterns  
- **Explainability**
  - Rule-aware explanations  
  - LLM-ready module  
- **Dataset** → IEEE-CIS Fraud Detection (1M+ transactions)

---

## 📦 Dataset: IEEE-CIS Fraud Detection

This project uses the public Kaggle dataset:

- `train_transaction.csv` — transaction-level data  
- `train_identity.csv` — device / metadata  
- `test_transaction.csv` — test transactions  
- `test_identity.csv` — test identity metadata  

> ⚠️ Dataset files are **NOT** included in this repo.  
> Download from Kaggle and place into:
---


## 📁 Project Structure

```text
llm-fraud-detection-assistant/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routes.py
│   ├── rules_engine.py
│   ├── llm_explainer.py
│   ├── models.py
│
├── models/
│   ├── fraud_model.pkl
│   ├── scaler.pkl
│
├── scripts/
│   ├── prepare_data.py
│   ├── train_model.py
│
├── docs/
│   ├── screenshot_homepage.png
│   ├── screenshot_result.png
│   ├── screenshot_VerySmallAmount_Explainer.png
│   ├── screenshot_HignAmount_Explainer.png
│   ├── screenshot_None_Explainer.png
│
├── requirements.txt
├── README.md
└── .gitignore
```
🟡 Very Small Amount — Rule Triggered  
![Very Small Amount](docs/screenshot_VerySmallAmount_Explainer.png)

🔴 High Amount — Multiple Rules Triggered  
![High Amount](docs/screenshot_HignAmount_Explainer.png)

🟢 Normal Transaction — No Rules Triggered  
![No Rules](docs/screenshot_None_Explainer.png)
```
