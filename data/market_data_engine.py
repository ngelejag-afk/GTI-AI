"""
GTI AI
Market Data Engine
Version 1.0
"""

from datetime import datetime

from models.market_data import MarketData


class MarketDataEngine:
    """
    Provides market data for GTI AI.
    """

    @staticmethod
    def sample() -> MarketData:
        """
        Return sample XAUUSD market data.
        """

        return MarketData(
            symbol="XAUUSD",
            timeframe="H1",
            timestamp=datetime.now(),
            open=3360.20,
            high=3367.80,
            low=3358.40,
            close=3365.90,
            volume=4521,
            spread=0.25,
        )
