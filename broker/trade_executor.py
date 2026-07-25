"""
GTI AI
Trade Executor
Version 1.0
"""

from broker.broker import Broker
from broker.order import Order
from broker.order_engine import OrderEngine


class TradeExecutor:
    """
    Executes trading orders through a broker.
    """

    def __init__(
        self,
        broker: Broker,
        order_engine: OrderEngine,
    ) -> None:
        self.broker = broker
        self.order_engine = order_engine

    def execute(self, order: Order) -> bool:
        """
        Execute a trading order.
        """

        if not self.broker.is_connected():
            return False

        self.order_engine.place(order)

        return True
