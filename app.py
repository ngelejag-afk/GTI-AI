"""
GTI AI
Main Application
Version 2.0
"""

from models.market import MarketContext

from analysis.trend import analyze_trend
from analysis.session import analyze_session
from analysis.location import analyze_location
from analysis.price_action import analyze_price_action
from analysis.news import analyze_news

from core.confidence_engine import ConfidenceEngine
from core.risk_engine import RiskEngine
from core.decision_engine import DecisionEngine
from core.explainability_engine import ExplainabilityEngine
from core.signal_engine import SignalEngine


def main() -> None:
    """
    GTI AI Entry Point
    """

    market = MarketContext(
        symbol="XAUUSD",
        timeframe="H1",
    )

    trend = analyze_trend(market)
    session = analyze_session(market)
    location = analyze_location(market)
    price_action = analyze_price_action(market)
    news = analyze_news(market)

    confidence = ConfidenceEngine(
        trend=30 if trend.upper() in ("BULLISH", "BEARISH") else 0,
        session=20 if session else 0,
        location=20 if location else 0,
        price_action=20 if price_action else 0,
        news=10 if news else 0,
    ).calculate()

    risk_allowed = RiskEngine(confidence).trade_allowed()

    decision = DecisionEngine(
        confidence,
        risk_allowed,
    ).decide()

    explanation = ExplainabilityEngine(
        decision,
        confidence,
        trend,
        str(session),
        str(location),
        str(price_action),
        str(news),
    ).generate()

    signal = SignalEngine(
        decision,
        confidence,
        explanation,
    ).generate()

    print(signal)


if __name__ == "__main__":
    main()
