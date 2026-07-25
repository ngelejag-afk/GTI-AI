"""
GTI AI
Trade Manager
Version 1.0
"""

from broker.position_engine import PositionEngine


class TradeManager:
    """
    Manages trading rules for open positions.
    """

    def __init__(self, positions: PositionEngine) -> None:
        self.positions = positions

    def can_open_trade(self) -> bool:
        """
        Return True if a new trade can be opened.
        """

        return self.positions.count() == 0

    def has_open_trade(self) -> bool:
        """
        Return True if there is an open trade.
        """

        return self.positions.count() > 0
