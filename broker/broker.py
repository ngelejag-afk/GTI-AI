"""
GTI AI
Broker Interface
Version 1.0
"""

from abc import ABC, abstractmethod


class Broker(ABC):
    """
    Base interface for broker integrations.
    """

    @abstractmethod
    def connect(self) -> bool:
        """
        Connect to the broker.
        """
        raise NotImplementedError

    @abstractmethod
    def disconnect(self) -> None:
        """
        Disconnect from the broker.
        """
        raise NotImplementedError

    @abstractmethod
    def is_connected(self) -> bool:
        """
        Return connection status.
        """
        raise NotImplementedError
