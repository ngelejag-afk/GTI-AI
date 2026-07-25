"""
GTI AI
Scenario Engine
Version 1.0
"""

from models.market import MarketContext


class ScenarioEngine:
    """
    Provides predefined market scenarios for testing.
    """

    @staticmethod
    def bullish() -> MarketContext:
        return MarketContext(
            symbol="XAUUSD",
            timeframe="H1",
            trend="BULLISH",
            session="LONDON",
            location="KEY_LEVEL",
            confirmation="BULLISH",
            news="SAFE",
        )

    @staticmethod
    def bearish() -> MarketContext:
        return MarketContext(
            symbol="XAUUSD",
            timeframe="H1",
            trend="BEARISH",
            session="NEW YORK",
            location="PULLBACK",
            confirmation="BEARISH",
            news="SAFE",
        )

    @staticmethod
    def no_trade() -> MarketContext:
        return MarketContext(
            symbol="XAUUSD",
            timeframe="H1",
            trend="SIDEWAYS",
            session="ASIA",
            location="NONE",
            confirmation="NONE",
            news="HIGH_IMPACT",
        )
