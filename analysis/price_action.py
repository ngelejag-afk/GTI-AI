"""
GTI AI
Price Action Analysis Engine
Version 1.0
"""

from models.market import MarketContext


def analyze_price_action(market: MarketContext) -> tuple[bool, str]:
    """
    Validate whether price action supports a trade.

    Returns:
        (approved, reason)
    """

    trend = market.trend.upper()
    structure = market.market_structure.upper()

    if trend == "BULLISH" and structure == "UPTREND":
        return True, "Bullish trend confirmed."

    if trend == "BEARISH" and structure == "DOWNTREND":
        return True, "Bearish trend confirmed."

    if structure == "SIDEWAYS":
        return False, "Market is ranging."

    return False, "Price action confirmation not found."
