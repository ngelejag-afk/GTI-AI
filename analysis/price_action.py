"""
GTI AI
Price Action Analysis Engine
Version 2.0
"""


class PriceActionEngine:
    """
    Determines whether price action confirms
    the current market direction.
    """

    def __init__(self, confirmation: str):
        self.confirmation = confirmation.strip().upper()

    def analyze(self) -> str:
        """
        Return the detected price action confirmation.
        """

        if self.confirmation == "BULLISH":
            return "Bullish Confirmation"

        if self.confirmation == "BEARISH":
            return "Bearish Confirmation"

        return "No Confirmation"

    def score(self) -> int:
        """
        Return confidence contribution.
        """

        if self.confirmation in ("BULLISH", "BEARISH"):
            return 20

        return 0

    def trade_allowed(self) -> bool:
        """
        Check whether price action supports trading.
        """

        return self.confirmation in ("BULLISH", "BEARISH")
