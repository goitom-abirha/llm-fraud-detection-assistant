# app/llm_explainer.py

from typing import List

def generate_explanation(amount: float, fraud_score: float, rules: List[str]) -> str:
    """
    Simple fallback explanation for the LLM fraud assistant.
    """

    rules_str = ", ".join(rules) if rules else "None"

    base = (
        f"Transaction amount: {amount}\n"
        f"Fraud score (0–1): {fraud_score:.4f}\n"
        f"Rules triggered: {rules_str}\n\n"
    )

    # Basic human-style reasoning
    if "HighAmount" in rules:
        base += "High transaction amount — could be risky. Review customer history."
    elif "VerySmallAmount" in rules:
        base += "Very small transaction — usually low risk."
    elif "SuspiciousRange_5k_6k" in rules:
        base += "Amount falls into a suspicious mid-range spike commonly used in fraud."
    elif "AvoidingThreshold" in rules:
        base += "Amount is just below a known review threshold — classic fraud evasion behavior."
    else:
        base += "No specific rules triggered. Looks like a normal transaction."

    return base
