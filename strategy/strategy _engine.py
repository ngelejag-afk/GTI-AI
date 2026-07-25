"""
GTI AI
Strategy Engine
Version 1.0
"""

from broker.order import Order
from strategy.base_strategy import BaseStrategy


class StrategyEngine:
    """
    Runs trading strategies.
    """

    def __init__(
        self,
        strategy: BaseStrategy,
    ) -> None:
        self.strategy = strategy

    def analyze(self) -> Order | None:
        """
        Execute the selected strategy.
        """

        return self.strategy.analyze()
