"""
GTI AI
Position Model
Version 1.0
"""

from dataclasses import dataclass


@dataclass
class Position:
    """
    Represents an open trading position.
    """

    ticket: int
    symbol: str

    position_type: str
    volume: float

    entry_price: float
    current_price: float

    stop_loss: float
    take_profit: float

    profit: float
