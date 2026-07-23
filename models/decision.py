"""
GTI AI Decision Model
"""

from dataclasses import dataclass


@dataclass
class Decision:
    action: str          # BUY, SELL, WAIT, NO_TRADE
    confidence: int
    reason: str
    approved: bool
