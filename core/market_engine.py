"""
GTI AI
Market Engine
Version 1.0
"""

from data.data_provider import DataProvider
from models.market_data import MarketData


class MarketEngine:
    """
    Central access point for market data.
    """

    def __init__(self, provider: DataProvider) -> None:
        self.provider = provider

    def latest(self) -> MarketData:
        """
        Return the latest market candle.
        """

        return self.provider.latest()

    def history(
        self,
        symbol: str,
        timeframe: str,
        candles: int,
    ) -> list[MarketData]:
        """
        Return market history.
        """

        return self.provider.history(
            symbol,
            timeframe,
            candles,
        )
