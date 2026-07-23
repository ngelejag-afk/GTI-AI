"""
GTI AI Decision Engine
"""

from models.decision import Decision


def make_decision(confidence: int, risk_ok: bool) -> Decision:
    """
    Makes the final trading decision.
    """

    if not risk_ok:
        return Decision(
            action="NO TRADE",
            confidence=confidence,
            reason="Risk rules failed.",
        )

    if confidence >= 80:
        return Decision(
            action="BUY",
            confidence=confidence,
            reason="High confidence and risk approved.",
        )

    return Decision(
        action="WAIT",
        confidence=confidence,
        reason="Confidence is not high enough.",
    )
