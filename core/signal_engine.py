"""
GTI AI
Signal Engine
Version 2.0
"""


class SignalEngine:
    """
    Generates the final GTI AI trading signal.
    """

    def __init__(
        self,
        decision: str,
        confidence: int,
        explanation: str,
    ) -> None:
        self.decision = decision
        self.confidence = confidence
        self.explanation = explanation

    def generate(self) -> str:
        """
        Return the final GTI AI signal.
        """

        return f"""
==============================
GTI AI SIGNAL
==============================

Decision   : {self.decision}

Confidence : {self.confidence}%

------------------------------

{self.explanation}

==============================
"""
