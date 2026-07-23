"""
GTI AI Signal Engine
"""

from models.signal import Signal
from models.decision import Decision


def generate_signal(decision: Decision) -> Signal:
    """Converts a decision into a trading signal."""

    return Signal(
        action=decision.action,
        confidence=decision.confidence,
        reason=decision.reason,
    )
