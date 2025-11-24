from flask import Blueprint, render_template_string, request
from .models import load_model, score_transaction
from .rules_engine import apply_rules

# ---------- Blueprint ----------
bp = Blueprint("main", __name__)

# Load model once (if you train one later)
model, scaler = load_model()

# ---------- HTML TEMPLATE ----------
INDEX_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>LLM Fraud Detection Assistant</title>
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f5f5f5;
            padding: 40px;
        }
        .container {
            max-width: 500px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        .result-box {
            margin-top: 15px;
            padding: 10px;
            background: #eef;
            border-radius: 6px;
        }
    </style>
</head>
<body>
<div class="container">
    <h1>LLM Fraud Detection Assistant</h1>
    <form method="post">
        <label class="form-label">Transaction amount:</label>
        <input type="number" step="0.01" name="amount" class="form-control" required />
        <button type="submit" class="btn btn-primary w-100 mt-3">Analyze</button>
    </form>
    {% if result %}
        <div class="result-box">
            <p><strong>Fraud score:</strong> {{ result.fraud_score }}</p>
            <p><strong>Rules triggered:</strong> {{ result.rules_triggered }}</p>
            <p><strong>Explanation:</strong></p>
            <pre>{{ result.explanation }}</pre>
        </div>
    {% endif %}
</div>
</body>
</html>
"""

# ---------- ROUTE ----------
@bp.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        # 1) Read user input
        amount = float(request.form.get("amount", 0.0))
        transaction = {"TransactionAmt": amount}

        # 2) Apply simple fraud rules
        rules = apply_rules(transaction)

        # 3) Get fraud score
        fraud_score = score_transaction(transaction, model, scaler)
        if fraud_score is None:
            # Demo score if no model trained yet
            fraud_score_display = f"{min(amount / 10000, 1):.4f} (demo score)"
        else:
            fraud_score_display = f"{fraud_score:.4f}"

        # 4) Simple explanation (no OpenAI yet)
        if "HighAmount" in rules:
            explanation = "High transaction amount — could be risky. Review customer history."
        elif "VerySmallAmount" in rules:
            explanation = "Very small transaction — usually low risk."
        else:
            explanation = "No specific rules triggered. Looks like a normal transaction."

        result = {
            "fraud_score": fraud_score_display,
            "rules_triggered": ", ".join(rules) if rules else "None",
            "explanation": explanation,
        }

    return render_template_string(INDEX_TEMPLATE, result=result)
