"""
GTI AI Market Model
"""

from dataclasses import dataclass


@dataclass
class MarketContext:
    symbol: str
    timeframe: str
    trend: str
    session: str
    news: bool
