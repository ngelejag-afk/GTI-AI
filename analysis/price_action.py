"""
GTI AI
Price Action Engine
"""

from models.market import MarketContext


def analyze_price_action(market: MarketContext) -> str:
    """
    Basic price action confirmation.
    """

    if market.trend.upper() == "BULLISH":
        return "BUY_CONFIRMATION"

    if market.trend.upper() == "BEARISH":
        return "SELL_CONFIRMATION"

    return "NO_CONFIRMATION"
