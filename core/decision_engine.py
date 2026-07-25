"""
GTI AI
Decision Engine
Version 2.0
"""


class DecisionEngine:
    """
    Makes the final GTI AI trading decision.
    """

    def __init__(
        self,
        confidence: int,
        risk_allowed: bool,
    ) -> None:
        self.confidence = confidence
        self.risk_allowed = risk_allowed

    def decide(self) -> str:
        """
        Return the final trading decision.
        """

        if not self.risk_allowed:
            return "NO TRADE"

        if self.confidence >= 90:
            return "BUY"

        if self.confidence >= 70:
            return "WAIT"

        return "NO TRADE"
