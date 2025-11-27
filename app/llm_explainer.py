from typing import List
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

client = None
if OPENAI_API_KEY:
    client = OpenAI(api_key=OPENAI_API_KEY)


def _fallback_explanation(amount: float, fraud_score: float, rules: List[str]) -> str:
    rules_str = ", ".join(rules) if rules else "None"

    base = (
        f"Transaction amount: {amount}\n"
        f"Fraud score (0–1): {fraud_score:.4f}\n"
        f"Rules triggered: {rules_str}\n\n"
    )

    if "HighAmount" in rules:
        base += "High transaction amount — could be risky. Review customer history."
    elif "VerySmallAmount" in rules:
        base += "Very small transaction — usually low risk."
    else:
        base += "No specific rules triggered. Looks like a normal transaction."

    return base


def generate_explanation(amount: float, fraud_score: float, rules: List[str]) -> str:
    # If no API key, use fallback
    if client is None:
        return _fallback_explanation(amount, fraud_score, rules)

    rules_str = ", ".join(rules) if rules else "None"

    prompt = f"""
You are a fraud analyst assistant at a bank.
Explain to a junior fraud analyst whether this transaction looks risky or normal.

Transaction details:
- Amount: {amount}
- Fraud score (0–1): {fraud_score:.4f}
- Rules triggered: {rules_str}

Instructions:
- Start with a one-sentence summary.
- Then give 2–3 bullet points explaining why.
- Use clear, non-technical language.
- Keep it under 150 words.
"""

    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt,
        )
        content = response.output[0].content[0].text
        return content
    except Exception as e:
        print(f"[WARN] OpenAI explanation failed: {e}")
        return _fallback_explanation(amount, fraud_score, rules)
