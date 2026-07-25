"""
GTI AI
Data Provider
Version 1.0
"""

from data.data_source import DataSource
from models.market_data import MarketData


class DataProvider:
    """
    Provides market data through a data source.
    """

    def __init__(self, source: DataSource) -> None:
        self.source = source

    def latest(self) -> MarketData:
        """
        Return the latest market candle.
        """

        return self.source.get_latest_candle()

    def history(
        self,
        symbol: str,
        timeframe: str,
        candles: int,
    ) -> list[MarketData]:
        """
        Return market history.
        """

        return self.source.get_history(
            symbol,
            timeframe,
            candles,
        )
