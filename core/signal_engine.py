"""
GTI AI
Signal Engine
"""

from models.signal import Signal


def generate_signal(decision: str) -> Signal:
    """
    Generate trading signal.
    """

    reasons = {
        "BUY": "Trend, confidence and risk requirements satisfied.",
        "SELL": "Bearish setup confirmed.",
        "WAIT": "Wait for better confirmation.",
        "NO TRADE": "Trade rules not satisfied.",
    }

    confidence = {
        "BUY": 85,
        "SELL": 85,
        "WAIT": 60,
        "NO TRADE": 40,
    }

    return Signal(
        action=decision,
        confidence=confidence.get(decision, 0),
        reason=reasons.get(decision, "Unknown"),
    )
