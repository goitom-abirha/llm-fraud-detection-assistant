# LLM Fraud Detection Assistant

A hybrid fraud detection system that combines **machine learning models**, **engineered fraud rules**, and a **Large Language Model (LLM)** to detect and explain suspicious financial transactions. Built using the **IEEE-CIS Fraud Detection Dataset**, this project simulates how real banks such as Capital One, Chase, Wells Fargo, and AmEx detect and investigate fraud.

---

##  Project Overview

Financial fraud is increasing in complexity due to device spoofing, account takeovers, identity theft, rapid-fire transactions, and cross-border payment risks. Traditional fraud scoring models lack transparency, and rule-based systems alone are not sufficient.

This project implements an **LLM-powered Fraud Detection Assistant** capable of:

- Scoring transactions using trained ML models  
- Identifying fraud signals using bank-style rule checks  
- Generating natural-language explanations using an LLM  
- Providing analysts with a simple case review dashboard  

This creates an **interpretable, explainable, and industry-aligned fraud detection workflow**.

---

##  Key Features

-  **Hybrid Risk Engine:** ML model + rules + LLM reasoning  
-  **Analyst Dashboard:** Search, explain, and review suspicious transactions  
-  **Machine Learning:** Logistic Regression, Random Forest, LightGBM  
-  **Bank-Style Fraud Rules:**  
  - New device / new IP  
  - Velocity checks  
  - Abnormal spending  
  - Browser/device mismatch  
  - Time-of-day anomalies  
-  **Explainable AI:** Generates clear explanations of why a transaction is risky  
-  **Realistic Dataset:** IEEE-CIS Fraud Detection (1M+ transactions)

---

##  Dataset: IEEE-CIS Fraud Detection

This project uses the public **IEEE-CIS Fraud Detection Dataset**:

- `train_transaction.csv` — main transaction data (with `isFraud`)  
- `train_identity.csv` — device/browser/IP identity metadata  
- `test_transaction.csv` — unlabeled transactions  
- `test_identity.csv` — identity metadata for test transactions  
- `sample_submission.csv` — Kaggle reference submission  

 *Due to size and licensing, raw dataset files are NOT uploaded to GitHub.*  
Download from Kaggle and place them inside:


---

##  Project Structure

The project follows a clean ML + LLM architecture.

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
│
├── .gitignore
├── requirements.txt
├── README.md

---

##  Progress Update — November 23, 2025

This is the initial working version of the LLM Fraud Detection Assistant.

###  Completed Today
- Set up full project folder structure  
- Added Flask app (`app/main.py`)  
- Added UI with Bootstrap  
- Implemented fraud rules (`HighAmount`, `VerySmallAmount`)  
- Added placeholder fraud scoring logic  
- Added LLM explanation module with fallback  
- Created static CSS + template structure  
- Verified app runs successfully at http://127.0.0.1:5000

## Screenshots

### 🏠 Home Page
![Home Page](docs/screenshot_homepage.png)

### 📊 Fraud Result Page
![Fraud Result](docs/screenshot_result.png)


More features will be added in upcoming development stages.

