"""
GTI AI
Risk Management Engine
"""

from models.trade import TradeSetup


def check_risk(trade: TradeSetup) -> bool:
    """
    Validate trade risk.
    """

    if trade.risk_percent > 1.0:
        return False

    risk = abs(trade.entry - trade.stop_loss)
    reward = abs(trade.take_profit - trade.entry)

    if reward < risk * 2:
        return False

    return True
