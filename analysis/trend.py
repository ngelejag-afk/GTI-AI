"""
GTI AI
Trend Analysis Engine
Version 1.0
"""

from models.market import MarketContext


def analyze_trend(market: MarketContext) -> str:
    """
    Analyze the overall market trend.

    Returns:
        "Bullish", "Bearish", or "Sideways"
    """

    trend = market.trend.strip().lower()

    if trend == "bullish":
        return "Bullish"

    if trend == "bearish":
        return "Bearish"

    return "Sideways"


def trend_score(trend: str) -> int:
    """
    Convert trend into a confidence score.
    """

    trend = trend.lower()

    if trend == "bullish":
        return 40

    if trend == "bearish":
        return 40

    return 0


def trend_is_tradeable(trend: str) -> bool:
    """
    Determine whether the trend is suitable for trading.
    """

    return trend.lower() in ("bullish", "bearish")
