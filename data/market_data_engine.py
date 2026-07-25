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
    @staticmethod
    def sample_history() -> list[MarketData]:
        """
        Return sample XAUUSD market history.
        """

        return [
            MarketData(
                symbol="XAUUSD",
                timeframe="H1",
                timestamp=datetime.now(),
                open=3358.20,
                high=3361.40,
                low=3356.90,
                close=3360.10,
                volume=4100,
                spread=0.25,
            ),
            MarketData(
                symbol="XAUUSD",
                timeframe="H1",
                timestamp=datetime.now(),
                open=3360.10,
                high=3364.80,
                low=3359.70,
                close=3363.50,
                volume=4320,
                spread=0.25,
            ),
            MarketData(
                symbol="XAUUSD",
                timeframe="H1",
                timestamp=datetime.now(),
                open=3363.50,
                high=3367.80,
                low=3362.90,
                close=3365.90,
                volume=4521,
                spread=0.25,
            ),
        ]
