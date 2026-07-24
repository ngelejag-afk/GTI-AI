"""
GTI AI
Decision Engine
"""


def make_decision(confidence: int, risk_ok: bool) -> str:
    """
    Make final trading decision.
    """

    if not risk_ok:
        return "NO TRADE"

    if confidence >= 80:
        return "BUY"

    if confidence >= 60:
        return "WAIT"

    return "NO TRADE"
