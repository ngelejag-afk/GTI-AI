"""
GTI AI Decision Engine
"""

from models.decision import Decision


def make_decision(confidence: int, risk_ok: bool) -> Decision:
    """Creates a trading decision."""

    if not risk_ok:
        return Decision(
            action="NO TRADE",
            confidence=confidence,
            reason="Risk exceeds limit.",
            approved=False,
        )

    if confidence >= 80:
        return Decision(
            action="BUY",
            confidence=confidence,
            reason="High confidence setup.",
            approved=True,
        )

    if confidence >= 60:
        return Decision(
            action="WAIT",
            confidence=confidence,
            reason="Need more confirmation.",
            approved=False,
        )

    return Decision(
        action="NO TRADE",
        confidence=confidence,
        reason="Low confidence.",
        approved=False,
    )
