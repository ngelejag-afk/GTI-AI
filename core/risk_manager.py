"""
GTI AI
Risk Manager
Version 1.0
"""

from broker.trade_manager import TradeManager
from broker.portfolio_engine import PortfolioEngine
from core.position_sizer import PositionSizer


class RiskManager:
    """
    Handles trading risk management.
    """

    def __init__(
        self,
        portfolio: PortfolioEngine,
        trade_manager: TradeManager,
    ) -> None:
        self.portfolio = portfolio
        self.trade_manager = trade_manager

    def can_trade(self) -> bool:
        """
        Return True if trading is allowed.
        """

        return self.trade_manager.can_open_trade()

    def calculate_lot(
        self,
        risk_percent: float,
        stop_loss_pips: float,
        pip_value: float,
    ) -> float:
        """
        Calculate the trading lot size.
        """

        account = self.portfolio.get()

        return PositionSizer.risk_based_lot(
            balance=account.balance,
            risk_percent=risk_percent,
            stop_loss_pips=stop_loss_pips,
            pip_value=pip_value,
        )
