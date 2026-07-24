"""
GTI AI
Location Analysis Engine
"""

from models.market import MarketContext


def analyze_location(market: MarketContext) -> str:
    """
    Analyze whether price is at a good trading location.
    """

    distance = abs(market.current_price - market.key_level)

    if distance <= 2.0:
        return "GOOD"

    if distance <= 5.0:
        return "AVERAGE"

    return "POOR"
