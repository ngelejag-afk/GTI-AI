"""
GTI AI Trade Model
"""

from dataclasses import dataclass


@dataclass
class TradeSetup:
    symbol: str
    direction: str
    entry: float
    stop_loss: float
    take_profit: float
    risk_percent: float
    reward_ratio: float
    confidence: int
    status: str
