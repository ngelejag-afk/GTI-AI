"""
GTI AI
Portfolio Model
Version 1.0
"""

from dataclasses import dataclass


@dataclass
class Portfolio:
    """
    Represents a trading account.
    """

    balance: float
    equity: float
    margin: float
    free_margin: float
    profit: float
