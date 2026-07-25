"""
GTI AI
Portfolio Engine
Version 1.0
"""

from broker.portfolio import Portfolio


class PortfolioEngine:
    """
    Manages the trading portfolio.
    """

    def __init__(self, portfolio: Portfolio) -> None:
        self.portfolio = portfolio

    def get(self) -> Portfolio:
        """
        Return the current portfolio.
        """

        return self.portfolio

    def update_profit(self, profit: float) -> None:
        """
        Update account profit and equity.
        """

        self.portfolio.profit = profit
        self.portfolio.equity = (
            self.portfolio.balance + profit
        )

    def deposit(self, amount: float) -> None:
        """
        Add funds to the account.
        """

        self.portfolio.balance += amount
        self.portfolio.equity += amount

    def withdraw(self, amount: float) -> None:
        """
        Remove funds from the account.
        """

        self.portfolio.balance -= amount
        self.portfolio.equity -= amount
