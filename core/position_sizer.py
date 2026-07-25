"""
GTI AI
Position Sizer
Version 1.0
"""


class PositionSizer:
    """
    Calculates trading lot size.
    """

    @staticmethod
    def fixed_lot(lot_size: float) -> float:
        """
        Return a fixed lot size.
        """

        return max(0.01, lot_size)

    @staticmethod
    def risk_based_lot(
        balance: float,
        risk_percent: float,
        stop_loss_pips: float,
        pip_value: float,
    ) -> float:
        """
        Calculate lot size based on account risk.
        """

        if stop_loss_pips <= 0 or pip_value <= 0:
            return 0.01

        risk_amount = balance * (risk_percent / 100)

        lot = risk_amount / (stop_loss_pips * pip_value)

        return round(max(0.01, lot), 2)
