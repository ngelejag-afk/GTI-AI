"""
GTI AI
Session Analysis Engine
Version 2.0
"""


class SessionEngine:
    """
    Determines whether the current trading session is favorable.
    """

    def __init__(self, session: str):
        self.session = session.strip().upper()

    def analyze(self) -> str:
        if self.session == "LONDON":
            return "London"

        if self.session == "NEW YORK":
            return "New York"

        if self.session == "LONDON_NEW_YORK":
            return "London + New York Overlap"

        return "Inactive"

    def score(self) -> int:
        if self.session in ("LONDON", "NEW YORK", "LONDON_NEW_YORK"):
            return 20

        return 0

    def trade_allowed(self) -> bool:
        return self.session in ("LONDON", "NEW YORK", "LONDON_NEW_YORK")
