"""
GTI AI
Position Engine
Version 1.0
"""

from broker.position import Position


class PositionEngine:
    """
    Manages open trading positions.
    """

    def __init__(self) -> None:
        self.positions: list[Position] = []

    def add(self, position: Position) -> None:
        """
        Add a new position.
        """

        self.positions.append(position)

    def all(self) -> list[Position]:
        """
        Return all open positions.
        """

        return self.positions

    def last(self) -> Position | None:
        """
        Return the latest position.
        """

        if not self.positions:
            return None

        return self.positions[-1]

    def count(self) -> int:
        """
        Return the number of open positions.
        """

        return len(self.positions)

    def clear(self) -> None:
        """
        Remove all positions.
        """

        self.positions.clear()
