"""
GTI AI
Base Strategy
Version 1.0
"""

from abc import ABC, abstractmethod

from broker.order import Order


class BaseStrategy(ABC):
    """
    Base interface for all trading strategies.
    """

    @abstractmethod
    def analyze(self) -> Order | None:
        """
        Analyze the market and return
        a trading order if a setup exists.
        """
        raise NotImplementedError
