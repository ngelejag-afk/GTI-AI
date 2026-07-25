"""
GTI AI
Risk Engine
Version 2.0
"""


class RiskEngine:
    """
    Determines whether a trade satisfies
    the minimum GTI AI confidence requirement.
    """

    MINIMUM_CONFIDENCE = 70

    def __init__(self, confidence: int) -> None:
        self.confidence = confidence

    def trade_allowed(self) -> bool:
        """
        Return True if the trade is allowed.
        """

        return self.confidence >= self.MINIMUM_CONFIDENCE
