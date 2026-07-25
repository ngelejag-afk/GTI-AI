"""
GTI AI
Confidence Engine
Version 2.0
"""


class ConfidenceEngine:
    """
    Calculates the overall GTI AI confidence score.
    """

    TREND_SCORE = 30
    SESSION_SCORE = 20
    LOCATION_SCORE = 20
    PRICE_ACTION_SCORE = 20
    NEWS_SCORE = 10

    def __init__(
        self,
        trend: int,
        session: int,
        location: int,
        price_action: int,
        news: int,
    ) -> None:
        self.trend = trend
        self.session = session
        self.location = location
        self.price_action = price_action
        self.news = news

    def calculate(self) -> int:
        """
        Return total confidence score.
        """

        return (
            self.trend
            + self.session
            + self.location
            + self.price_action
            + self.news
        )
