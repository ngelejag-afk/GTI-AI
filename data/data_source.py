"""
GTI AI
Data Source
Version 1.0
"""

from abc import ABC, abstractmethod

from models.market_data import MarketData


class DataSource(ABC):
    """
    Base class for all market data sources.
    """

    @abstractmethod
    def get_latest_candle(self) -> MarketData:
        """
        Return the latest market candle.
        """
        raise NotImplementedError

    @abstractmethod
    def get_history(
        self,
        symbol: str,
        timeframe: str,
        candles: int,
    ) -> list[MarketData]:
        """
        Return market history.
        """
        raise NotImplementedError
