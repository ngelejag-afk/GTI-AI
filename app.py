"""
GTI AI
Main Application Entry Point
Version 0.2
"""

from models.market import MarketContext

from analysis.trend import analyze_trend
from analysis.session import analyze_session
from analysis.location import analyze_location
from analysis.price_action import analyze_price_action
from analysis.news import analyze_news

from core.confidence_engine import calculate_confidence
from core.risk_engine import check_risk
from core.decision_engine import make_decision
from core.explainability_engine import generate_explanation
from core.signal_engine import generate_signal


def main() -> None:
    """
    GTI AI Demo
    """

    market = MarketContext(
        symbol="XAUUSD",
        timeframe="H1",
        trend="Bullish",
        session="London",
        market_structure="Uptrend",
        key_level=2350.00,
        current_price=2348.20,
        news=False,
    )

    trend = analyze_trend(market)
    session_ok, session_reason = analyze_session(market)
    location_ok, location_reason = analyze_location(market)
    price_action_ok, price_action_reason = analyze_price_action(market)
    news_ok, news_reason = analyze_news(market)

    print("=" * 50)
    print("GTI AI MARKET ANALYSIS")
    print("=" * 50)

    print(f"Trend          : {trend}")
    print(f"Session        : {session_reason}")
    print(f"Location       : {location_reason}")
    print(f"Price Action   : {price_action_reason}")
    print(f"News           : {news_reason}")
