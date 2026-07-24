"""
GTI AI
Decision Engine
Version 1.0
"""


def make_decision(
    confidence: int,
    risk_ok: bool,
) -> str:
    """
    Make the final trading decision.

    Returns:
        BUY
        WAIT
        NO TRADE
    """

    if not risk_ok:
        return "NO TRADE"

    if confidence >= 90:
        return "BUY"

    if confidence >= 70:
        return "WAIT"

    return "NO TRADE"
