"""
GTI AI
Trend Analysis Engine
"""

from models.market import MarketContext


def analyze_trend(market: MarketContext) -> str:
    """
    Returns the market trend.
    """

    if market.trend.upper() == "UP":
        return "BUY"

    if market.trend.upper() == "DOWN":
        return "SELL"

    return "WAIT"
