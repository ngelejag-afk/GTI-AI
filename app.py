"""
GTI AI
Main Application Entry Point
Version 1.0
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
    """Run a complete GTI AI market analysis."""

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

    confidence = calculate_confidence(
        trend=trend,
        session=session_ok,
        location=location_ok,
        price_action=price_action_ok,
        news=news_ok,
    )

    risk_ok = check_risk(confidence)

    decision = make_decision(
        confidence=confidence,
        risk_ok=risk_ok,
    )

    explanation = generate_explanation(
        decision=decision,
        confidence=confidence,
        trend=trend,
        session=session_reason,
        location=location_reason,
        price_action=price_action_reason,
        news=news_reason,
    )

    signal = generate_signal(
        decision=decision,
        confidence=confidence,
        explanation=explanation,
    )

    print("=" * 60)
    print("GTI AI MARKET ANALYSIS")
    print("=" * 60)

    print(f"Symbol          : {market.symbol}")
    print(f"Timeframe       : {market.timeframe}")
    print(f"Trend           : {trend}")
    print(f"Session         : {session_reason}")
    print(f"Location        : {location_reason}")
    print(f"Price Action    : {price_action_reason}")
    print(f"News            : {news_reason}")

    print("=" * 60)
    print("FINAL DECISION")
    print("=" * 60)

    print(signal)

    print("=" * 60)
    print("EXPLANATION")
    print("=" * 60)

    print(explanation)


if __name__ == "__main__":
    main()
