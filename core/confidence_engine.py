"""
GTI AI
Confidence Engine
"""

from models.market import MarketContext


def calculate_confidence(market: MarketContext) -> int:
    """
    Calculate confidence score.
    """

    score = 50

    if market.trend.upper() == "BULLISH":
        score += 20

    if market.session.upper() in ["LONDON", "NEW YORK"]:
        score += 15

    if not market.news:
        score += 15

    return min(score, 100)
