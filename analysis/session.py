"""
GTI AI
Session Analysis Engine
"""

from models.market import MarketContext


def analyze_session(market: MarketContext) -> str:
    """
    Determines whether the current trading session is favorable.
    """

    session = market.session.upper()

    if session in ["LONDON", "NEW YORK"]:
        return "ACTIVE"

    if session == "ASIAN":
        return "SLOW"

    return "UNKNOWN"
