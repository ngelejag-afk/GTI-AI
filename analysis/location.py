"""
GTI AI
Location Analysis Engine
Version 2.0
"""


class LocationEngine:
    """
    Determines whether price is at a high-probability trading location.
    """

    def __init__(self, location: str):
        self.location = location.strip().upper()

    def analyze(self) -> str:
        if self.location == "KEY_LEVEL":
            return "Key Support/Resistance"

        if self.location == "PULLBACK":
            return "Healthy Pullback"

        return "Poor Location"

    def score(self) -> int:
        if self.location in ("KEY_LEVEL", "PULLBACK"):
            return 20

        return 0

    def trade_allowed(self) -> bool:
        return self.location in ("KEY_LEVEL", "PULLBACK")
