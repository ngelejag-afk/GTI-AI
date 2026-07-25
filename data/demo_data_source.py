"""
GTI AI
Demo Data Source
Version 1.0
"""

from data.data_source import DataSource
from data.market_data_engine import MarketDataEngine
from models.market_data import MarketData


class DemoDataSource(DataSource):
    """
    Demo implementation of a market data source.
    """

    def get_latest_candle(self) -> MarketData:
        """
        Return the latest sample candle.
        """

        return MarketDataEngine.sample()

    def get_history(
        self,
        symbol: str,
        timeframe: str,
        candles: int,
    ) -> list[MarketData]:
        """
        Return sample market history.
        """

        return MarketDataEngine.sample_history()
