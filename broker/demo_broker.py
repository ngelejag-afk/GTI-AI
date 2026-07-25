"""
GTI AI
Demo Broker
Version 1.0
"""

from broker.broker import Broker


class DemoBroker(Broker):
    """
    Demo implementation of a broker.
    """

    def __init__(self) -> None:
        self._connected = False

    def connect(self) -> bool:
        """
        Connect to the demo broker.
        """

        self._connected = True
        return True

    def disconnect(self) -> None:
        """
        Disconnect from the demo broker.
        """

        self._connected = False

    def is_connected(self) -> bool:
        """
        Return connection status.
        """

        return self._connected
