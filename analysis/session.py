"""
GTI AI
Session Analysis Engine
Version 1.0
"""

from models.market import MarketContext


def analyze_session(market: MarketContext) -> tuple[bool, str]:
    """
    Check whether the current trading session is suitable.

    Returns:
        (approved, reason)
    """

    session = market.session.strip().upper()

    if session == "LONDON":
        return True, "London session is active."

    if session == "NEW YORK":
        return True, "New York session is active."

    if session == "LONDON-NEW YORK":
        return True, "London/New York overlap detected."

    if session == "ASIAN":
        return False, "Asian session has lower volatility."

    return False, f"Unknown trading session: {market.session}"
