"""
GTI AI
Order Model
Version 1.0
"""

from dataclasses import dataclass


@dataclass
class Order:
    """
    Represents a trading order.
    """

    symbol: str
    order_type: str
    volume: float

    entry_price: float
    stop_loss: float
    take_profit: float
