"""
GTI AI
Market Data Model
Version 1.0
"""


from dataclasses import dataclass
from datetime import datetime


@dataclass
class MarketData:
    """
    Represents one XAUUSD market candle.
    """

    symbol: str
    timeframe: str
    timestamp: datetime

    open: float
    high: float
    low: float
    close: float

    volume: float
    spread: float
