"""
GTI AI
Signal Engine

Creates a trading signal from the final decision.
"""

from models.signal import Signal


def generate_signal(decision: str) -> Signal:
    """
    Generate a Signal object from the trading decision.
    """

    reasons = {
        "BUY": (
            "Trend is bullish, confidence is high, "
            "risk rules passed and market conditions are favorable."
        ),
        "SELL": (
            "Trend is bearish, confidence is high, "
            "risk rules passed and market conditions are favorable."
        ),
        "WAIT": (
            "Market confirmation is not strong enough. "
            "Wait for a better setup."
        ),
        "NO TRADE": (
            "One or more GTI AI trading rules failed."
        ),
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
        reason=reasons.get(decision, "Unknown decision."),
    )
