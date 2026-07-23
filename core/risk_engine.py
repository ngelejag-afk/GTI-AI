"""
GTI AI Risk Engine
"""


def validate_risk(risk_percent: float) -> bool:
    """
    Returns True if risk is within the allowed limit.
    """

    return 0 < risk_percent <= 1.0
