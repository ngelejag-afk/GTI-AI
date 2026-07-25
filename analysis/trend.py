"""
GTI AI
Trend Analysis Engine
Version 2.0
"""


class TrendEngine:
    """
    Determines the higher timeframe market trend.
    """

    def __init__(self, timeframe: str, trend: str):
        self.timeframe = timeframe
        self.trend = trend.strip().upper()

    def analyze(self) -> str:
        """
        Return the detected trend.
        """

        if self.trend == "BULLISH":
            return "Bullish"

        if self.trend == "BEARISH":
            return "Bearish"

        return "Sideways"

    def score(self) -> int:
        """
        Return confidence contribution.
        """

        if self.trend in ("BULLISH", "BEARISH"):
            return 30

        return 0

    def trade_allowed(self) -> bool:
        """
        Check whether trading is allowed.
        """

        return self.trend in ("BULLISH", "BEARISH")
