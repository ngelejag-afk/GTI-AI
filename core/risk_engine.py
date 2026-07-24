"""
GTI AI
Risk Engine
Version 1.0
"""


def check_risk(confidence: int) -> bool:
    """
    Determine whether a trade passes the minimum confidence requirement.

    Returns:
        True if trade is allowed.
        False otherwise.
    """

    MINIMUM_CONFIDENCE = 70

    return confidence >= MINIMUM_CONFIDENCE
