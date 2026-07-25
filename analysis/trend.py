"""
GTI AI
Trend Engine
Version 3.0
"""

from models.market_data import MarketData


class TrendEngine:
    """
    Determines the market trend
    from XAUUSD candle data.
    """

    def __init__(self, market_data: MarketData) -> None:
        self.market_data = market_data

    def analyze(self) -> str:
        """
        Analyze the current candle.
        """

        if self.market_data.close > self.market_data.open:
            return "BULLISH"

        if self.market_data.close < self.market_data.open:
            return "BEARISH"

        return "SIDEWAYS"

    def score(self) -> int:
        """
        Return the trend confidence score.
        """

        trend = self.analyze()

        if trend in ("BULLISH", "BEARISH"):
            return 30

        return 0

    def trade_allowed(self) -> bool:
        """
        Return True if a trend exists.
        """

        return self.analyze() != "SIDEWAYS"
