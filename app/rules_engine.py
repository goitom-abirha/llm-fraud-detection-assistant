from typing import List, Dict

def apply_rules(transaction: Dict) -> List[str]:
    rules = []

    amount = float(transaction.get("TransactionAmt", 0.0))

    # ---------------------------------
    #  FRAUD RULES (Multiple Conditions)
    # ---------------------------------

    # Rule 1 – Very large amount
    if amount >= 5000:
        rules.append("HighAmount")

    # Rule 2 – Extremely small or suspicious micro-payment
    if amount <= 1:
        rules.append("VerySmallAmount")

    # Rule 3 – Mid-range suspicious range
    if 5000 < amount < 6000:
        rules.append("SuspiciousRange_5k_6k")

    # Rule 4 – Amount ends with repeating digits (e.g. 9999, 7777)
    if str(int(amount)).endswith(("000", "999", "777")):
        rules.append("RepeatingPatternAmount")

    # Rule 5 – Too rounded (e.g. 100, 2000, 5000)
    if amount % 1000 == 0:
        rules.append("TooRoundedAmount")

    # Rule 6 – Slightly below threshold (common fraud trick)
    if 4900 <= amount <= 4999:
        rules.append("AvoidingThreshold")

    return rules

