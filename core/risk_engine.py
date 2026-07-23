"""
GTI AI Risk Engine
"""

from models.trade import TradeSetup


def check_risk(trade: TradeSetup) -> bool:
    """
    Validates whether the trade satisfies risk rules.
    """

    if trade.risk_percent > 1.0:
        return False

    if trade.stop_loss <= 0:
        return False

    if trade.take_profit <= trade.entry:
        return False

    return True
