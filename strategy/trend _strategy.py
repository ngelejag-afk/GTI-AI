"""
GTI AI
Trend Strategy
Version 1.0
"""

from analysis.trend import TrendEngine
from broker.order import Order
from models.market_data import MarketData
from strategy.base_strategy import BaseStrategy


class TrendStrategy(BaseStrategy):
    """
    Simple trend-following strategy.
    """

    def __init__(
        self,
        history: list[MarketData],
        symbol: str,
    ) -> None:
        self.history = history
        self.symbol = symbol

    def analyze(self) -> Order | None:
        """
        Return a BUY or SELL order
        if a valid trend exists.
        """

        trend = TrendEngine(self.history).analyze()

        if trend == "BULLISH":
            return Order(
                symbol=self.symbol,
                order_type="BUY",
                volume=0.01,
                entry_price=0.0,
                stop_loss=0.0,
                take_profit=0.0,
            )

        if trend == "BEARISH":
            return Order(
                symbol=self.symbol,
                order_type="SELL",
                volume=0.01,
                entry_price=0.0,
                stop_loss=0.0,
                take_profit=0.0,
            )

        return None
