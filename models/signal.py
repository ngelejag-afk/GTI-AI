"""
GTI AI Signal Model
"""

from dataclasses import dataclass


@dataclass
class Signal:
    symbol: str
    action: str
    entry: float
    stop_loss: float
    take_profit: float
    confidence: int
    explanation: str
    timestamp: str
