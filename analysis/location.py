"""
GTI AI
Location Analysis Engine
Version 1.0
"""

from models.market import MarketContext


def analyze_location(market: MarketContext) -> tuple[bool, str]:
    """
    Check whether the current price is at a valid trading location.

    Returns:
        (approved, reason)
    """

    current = market.current_price
    level = market.key_level

    distance = abs(current - level)

    if distance <= 5:
        return True, "Price is at a key support/resistance level."

    if distance <= 15:
        return True, "Price is close to a key level."

    return False, "Price is too far from the nearest key level."
