"""
GTI AI
Main Application
Version 2.2
"""

from core.scenario_engine import ScenarioEngine

from analysis.trend import TrendEngine
from analysis.session import SessionEngine
from analysis.location import LocationEngine
from analysis.price_action import PriceActionEngine
from analysis.news import NewsEngine

from core.confidence_engine import ConfidenceEngine
from core.risk_engine import RiskEngine
from core.decision_engine import DecisionEngine
from core.explainability_engine import ExplainabilityEngine
from core.signal_engine import SignalEngine


def main() -> None:
    """
    GTI AI Entry Point
    """

    # Change this line to test different scenarios:
    # ScenarioEngine.bullish()
    # ScenarioEngine.bearish()
    # ScenarioEngine.no_trade()
    market = ScenarioEngine.bearish()

    trend_engine = TrendEngine(
        market.timeframe,
        market.trend,
    )

    session_engine = SessionEngine(
        market.session,
    )

    location_engine = LocationEngine(
        market.location,
    )

    price_action_engine = PriceActionEngine(
        market.confirmation,
    )

    news_engine = NewsEngine(
        market.news,
    )

    trend = trend_engine.analyze()
    session = session_engine.analyze()
    location = location_engine.analyze()
    price_action = price_action_engine.analyze()
    news = news_engine.analyze()

    confidence = ConfidenceEngine(
        trend=trend_engine.score(),
        session=session_engine.score(),
        location=location_engine.score(),
        price_action=price_action_engine.score(),
        news=news_engine.score(),
    ).calculate()

    risk_allowed = RiskEngine(
        confidence,
    ).trade_allowed()

    decision = DecisionEngine(
        confidence,
        risk_allowed,
    ).decide()

    explanation = ExplainabilityEngine(
        decision,
        confidence,
        trend,
        session,
        location,
        price_action,
        news,
    ).generate()

    signal = SignalEngine(
        decision,
        confidence,
        explanation,
    ).generate()

    print(signal)


if __name__ == "__main__":
    main()
