"""
GTI AI
Trend Engine
Version 4.0
"""

from analysis.indicators import IndicatorsEngine
from models.market_data import MarketData


class TrendEngine:
    """
    Determines the market trend
    using moving averages.
    """

    def __init__(self, history: list[MarketData]) -> None:
        self.history = history

    def analyze(self) -> str:
        """
        Analyze the market trend.
        """

        ema20 = IndicatorsEngine.ema(self.history, 20)
        ema50 = IndicatorsEngine.ema(self.history, 50)

        if ema20 == 0.0 or ema50 == 0.0:
            return "UNKNOWN"

        if ema20 > ema50:
            return "BULLISH"

        if ema20 < ema50:
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
        Return True if a valid trend exists.
        """

        return self.analyze() in ("BULLISH", "BEARISH")
