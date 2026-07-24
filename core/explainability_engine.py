"""
GTI AI
Explainability Engine
Version 1.0
"""


def generate_explanation(
    decision: str,
    confidence: int,
    trend: str,
    session: str,
    location: str,
    price_action: str,
    news: str,
) -> str:
    """
    Generate a human-readable explanation
    for the final trading decision.
    """

    return f"""
Decision      : {decision}

Confidence    : {confidence}%

Trend         : {trend}
Session       : {session}
Location      : {location}
Price Action  : {price_action}
News          : {news}

GTI AI Recommendation:
The decision was generated after evaluating
trend, session, key location, price action,
and market news.
"""
