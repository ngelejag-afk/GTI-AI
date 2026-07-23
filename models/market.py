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
    market_structure: str
    key_level: float
    current_price: float
    news: bool
