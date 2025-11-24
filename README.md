# LLM Fraud Detection Assistant

A hybrid fraud detection system that combines **machine learning models**, **engineered fraud rules**, and a **Large Language Model (LLM)** to detect and explain suspicious financial transactions. Built using the **IEEE-CIS Fraud Detection Dataset**, this project simulates how real banks such as Capital One, Chase, Wells Fargo, and AmEx detect and investigate fraud.

---

## Project Overview

Financial fraud is increasing in complexity due to device spoofing, account takeovers, identity theft, rapid-fire transactions, and cross-border payment risks. Traditional fraud scoring models lack transparency, and rule-based systems alone are not sufficient.

This project implements an **LLM-powered Fraud Detection Assistant** capable of:

- Scoring transactions using trained ML models  
- Identifying fraud signals using bank-style rule checks  
- Generating natural-language explanations using an LLM  
- Providing analysts with a simple case review dashboard  

This creates an **interpretable, explainable, and industry-aligned fraud detection workflow**.

---

## Key Features

- **Hybrid Risk Engine:** ML model + rules + LLM reasoning  
- **Analyst Dashboard:** Search, explain, and review suspicious transactions  
- **Machine Learning:** Logistic Regression, Random Forest, LightGBM  
- **Bank-Style Fraud Rules:**  
  - New device / new IP  
  - Velocity checks  
  - Abnormal spending  
  - Browser/device mismatch  
  - Time-of-day anomalies  
- **Explainable AI:** Generates clear explanations of why a transaction is risky  
- **Realistic Dataset:** IEEE-CIS Fraud Detection (1M+ transactions)

---

## Dataset: IEEE-CIS Fraud Detection

This project uses the public **IEEE-CIS Fraud Detection Dataset**.

> ⚠️ *Raw datasets are NOT uploaded to GitHub due to size and Kaggle license restrictions.*  
> Download from Kaggle and place inside `data/raw/`.

---

## Project Structure

```text
llm-fraud-detection-assistant/
│
├── data/
│   ├── raw/                # Raw IEEE-CIS dataset (NOT uploaded)
│   ├── processed/          # Cleaned & merged datasets
│
├── notebooks/
│   ├── 01_eda.ipynb                # Exploratory Data Analysis
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│
├── app/
│   ├── __init__.py
│   ├── main.py                    # Flask/Streamlit main app
│   ├── rules_engine.py            # Bank-style fraud rules
│   ├── llm_explainer.py           # OpenAI LLM prompts + reasoning
│   ├── models.py                  # ML model loading + scoring
│
├── models/
│   ├── fraud_model.pkl            # Trained ML model
│   ├── scaler.pkl
│
├── scripts/
│   ├── prepare_data.py            # Data cleaning + merging
│   ├── train_model.py
│
├── docs/
│   ├── proposal.pdf
│   ├── architecture_diagram.png
│   ├── screenshot_homepage.png
│   ├── screenshot_result.png
│
├── .gitignore
├── requirements.txt
├── README.md
