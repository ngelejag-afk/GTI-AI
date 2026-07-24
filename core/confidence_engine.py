"""
GTI AI
Confidence Engine
Version 1.0
"""


def calculate_confidence(
    trend: str,
    session: bool,
    location: bool,
    price_action: bool,
    news: bool,
) -> int:
    """
    Calculate GTI AI confidence score.

    Returns:
        Confidence percentage (0-100)
    """

    score = 0

    # Trend
    if trend.upper() in ("BULLISH", "BEARISH"):
        score += 30

    # Trading Session
    if session:
        score += 20

    # Key Level / Location
    if location:
        score += 20

    # Price Action
    if price_action:
        score += 20

    # No High Impact News
    if news:
        score += 10

    return score
