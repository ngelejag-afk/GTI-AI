"""
GTI AI
Order Engine
Version 1.0
"""

from broker.order import Order


class OrderEngine:
    """
    Handles trading orders.
    """

    def __init__(self) -> None:
        self.orders: list[Order] = []

    def place(self, order: Order) -> None:
        """
        Store a new trading order.
        """

        self.orders.append(order)

    def all(self) -> list[Order]:
        """
        Return all trading orders.
        """

        return self.orders

    def last(self) -> Order | None:
        """
        Return the most recent order.
        """

        if not self.orders:
            return None

        return self.orders[-1]
