"""
GTI AI
News Analysis Engine
Version 2.0
"""


class NewsEngine:
    """
    Determines whether market news allows trading.
    """

    def __init__(self, news: str):
        self.news = news.strip().upper()

    def analyze(self) -> str:
        if self.news == "SAFE":
            return "No High Impact News"

        if self.news == "HIGH_IMPACT":
            return "High Impact News"

        return "Unknown"

    def score(self) -> int:
        if self.news == "SAFE":
            return 10

        return 0

    def trade_allowed(self) -> bool:
        return self.news == "SAFE"
