"""
GTI AI
News Analysis Engine
"""

from models.market import MarketContext


def analyze_news(market: MarketContext) -> str:
    """
    Checks if high-impact news is present.
    """

    if market.news:
        return "BLOCK"

    return "CLEAR"
