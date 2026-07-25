
"""
GTI AI
Indicators Engine
Version 2.0
"""

from models.market_data import MarketData


class IndicatorsEngine:
    """
    Calculates technical indicators
    used by GTI AI.
    """

    @staticmethod
    def closing_prices(history: list[MarketData]) -> list[float]:
        """
        Return closing prices.
        """

        return [candle.close for candle in history]

    @staticmethod
    def sma(history: list[MarketData]) -> float:
        """
        Return the Simple Moving Average.
        """

        closes = IndicatorsEngine.closing_prices(history)

        if not closes:
            return 0.0

        return sum(closes) / len(closes)

    @staticmethod
    def ema(
        history: list[MarketData],
        period: int,
    ) -> float:
        """
        Return the Exponential Moving Average.
        """

        closes = IndicatorsEngine.closing_prices(history)

        if len(closes) < period:
            return 0.0

        closes = closes[-period:]

        multiplier = 2 / (period + 1)

        ema = closes[0]

        for price in closes[1:]:
            ema = (price - ema) * multiplier + ema

        return ema
