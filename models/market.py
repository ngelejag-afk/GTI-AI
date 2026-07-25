"""
GTI AI
Market Context
Version 2.0
"""


class MarketContext:
    """
    Holds all market information required by GTI AI.
    """

    def __init__(
        self,
        symbol: str,
        timeframe: str,
        trend: str,
        session: str,
        location: str,
        confirmation: str,
        news: str,
    ) -> None:
        self.symbol = symbol
        self.timeframe = timeframe
        self.trend = trend
        self.session = session
        self.location = location
        self.confirmation = confirmation
        self.news = news
