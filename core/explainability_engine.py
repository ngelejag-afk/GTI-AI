"""
GTI AI
Explainability Engine
Version 2.0
"""


class ExplainabilityEngine:
    """
    Generates a human-readable explanation
    for the GTI AI decision.
    """

    def __init__(
        self,
        decision: str,
        confidence: int,
        trend: str,
        session: str,
        location: str,
        price_action: str,
        news: str,
    ) -> None:
        self.decision = decision
        self.confidence = confidence
        self.trend = trend
        self.session = session
        self.location = location
        self.price_action = price_action
        self.news = news

    def generate(self) -> str:
        """
        Return the final explanation.
        """

        return f"""
Decision      : {self.decision}

Confidence    : {self.confidence}%

Trend         : {self.trend}
Session       : {self.session}
Location      : {self.location}
Price Action  : {self.price_action}
News          : {self.news}

GTI AI Recommendation:
The decision was generated after evaluating
trend, session, key location, price action,
and market news.
"""
