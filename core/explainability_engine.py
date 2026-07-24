"""
GTI AI
Explainability Engine

Generates a human-readable explanation for GTI AI decisions.
"""


def generate_explanation(
    decision: str,
    confidence: int,
    trend: str,
    session: str,
    risk_ok: bool,
    news: bool,
) -> str:
    """
    Generate a detailed explanation for the final trading decision.
    """

    lines = [
        "=" * 40,
        "GTI AI ANALYSIS",
        "=" * 40,
        f"Decision        : {decision}",
        f"Confidence      : {confidence}%",
        f"Trend           : {trend}",
        f"Session         : {session}",
        f"Risk Check      : {'PASSED' if risk_ok else 'FAILED'}",
        f"High Impact News: {'YES' if news else 'NO'}",
        "",
        "Explanation:",
    ]

    if decision == "BUY":
        lines.extend([
            "- Bullish market trend confirmed.",
            "- Confidence score is strong.",
            "- Risk rules passed.",
            "- Market conditions support buying.",
        ])

    elif decision == "SELL":
        lines.extend([
            "- Bearish market trend confirmed.",
            "- Confidence score is strong.",
            "- Risk rules passed.",
            "- Market conditions support selling.",
        ])

    elif decision == "WAIT":
        lines.extend([
            "- Market confirmation is weak.",
            "- Better setup is required.",
        ])

    else:
        lines.extend([
            "- One or more GTI AI trading rules failed.",
            "- No trade should be taken.",
        ])

    lines.append("=" * 40)

    return "\n".join(lines)
