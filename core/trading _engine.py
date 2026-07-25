"""
GTI AI
Trading Engine
Version 1.0
"""

from broker.order import Order
from broker.trade_executor import TradeExecutor
from core.risk_manager import RiskManager


class TradingEngine:
    """
    Coordinates trade execution.
    """

    def __init__(
        self,
        executor: TradeExecutor,
        risk_manager: RiskManager,
    ) -> None:
        self.executor = executor
        self.risk_manager = risk_manager

    def execute(self, order: Order) -> bool:
        """
        Execute a trade if allowed.
        """

        if not self.risk_manager.can_trade():
            return False

        return self.executor.execute(order)
