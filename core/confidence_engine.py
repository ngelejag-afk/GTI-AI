"""
GTI AI Confidence Engine
"""

from models.market import MarketContext


def calculate_confidence(market: MarketContext) -> int:
    """
    Calculates confidence score based on market conditions.
    """

    score = 50

    if market.trend.lower() == "bullish":
        score += 20

    if market.session.lower() in ("london", "new york"):
        score += 20

    if not market.news:
        score += 10

    return min(score, 100)
