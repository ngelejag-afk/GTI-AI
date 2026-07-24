"""
GTI AI
Explainability Engine
"""


def explain_decision(
    decision: str,
    trend: str,
    session: str,
    confidence: int,
    risk_ok: bool,
    news: bool,
) -> str:
    """
    Generate a human-readable explanation for the trading decision.
    """

    reasons = []

    reasons.append(f"Trend: {trend}")
    reasons.append(f"Session: {session}")
    reasons.append(f"Confidence Score: {confidence}%")
    reasons.append(f"Risk Check: {'Passed' if risk_ok else 'Failed'}")
    reasons.append(
        f"High Impact News: {'Yes' if news else 'No'}"
    )

    if decision == "BUY":
        summary = (
            "BUY because trend is bullish, risk rules passed, "
            "confidence is strong and market conditions are favorable."
        )

    elif decision == "SELL":
        summary = (
            "SELL because trend is bearish, risk rules passed, "
            "confidence is strong and market conditions are favorable."
        )

    elif decision == "WAIT":
        summary = (
            "WAIT because confirmation is not strong enough."
        )

    else:
        summary = (
            "NO TRADE because one or more GTI AI rules failed."
        )

    return "\n".join(reasons) + "\n\nExplanation:\n" + summary
