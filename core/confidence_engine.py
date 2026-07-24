"""
GTI AI
Confidence Engine

Calculates confidence score for a trade setup.
"""

from models.market import MarketContext


def calculate_confidence(market: MarketContext) -> int:
    """
    Calculate confidence score from market conditions.

    Returns:
        int: Confidence score (0-100)
    """

    score = 0

    # Trend
    if market.trend.lower() == "bullish":
        score += 25
    elif market.trend.lower() == "bearish":
        score += 25

    # Market Structure
    if market.market_structure.lower() in ("uptrend", "downtrend"):
        score += 20

    # Trading Session
    if market.session.lower() in ("london", "new york"):
        score += 20

    # News Filter
    if not market.news:
        score += 20

    # Price near key level
    distance = abs(market.current_price - market.key_level)

    if distance <= 5:
        score += 15

    return min(score, 100)
