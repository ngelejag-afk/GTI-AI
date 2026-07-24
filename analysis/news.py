"""
GTI AI
News Analysis Engine
Version 1.0
"""

from models.market import MarketContext


def analyze_news(market: MarketContext) -> tuple[bool, str]:
    """
    Check whether high-impact news blocks trading.

    Returns:
        (approved, reason)
    """

    if market.news:
        return False, "High-impact news detected."

    return True, "No high-impact news."
