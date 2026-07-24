"""
GTI AI
Main Application Entry Point
Version 0.1
"""

from datetime import datetime

from models.market import MarketContext
from models.trade import TradeSetup

from core.confidence_engine import calculate_confidence
from core.risk_engine import check_risk
from core.decision_engine import make_decision
from core.explainability_engine import generate_explanation
from core.signal_engine import generate_signal


def main() -> None:
    """
    GTI AI demo.
    """

    market = MarketContext(
        symbol="XAUUSD",
        timeframe="H1",
        trend="Bullish",
        session="London",
        market_structure="Uptrend",
        key_level=2350.00,
        current_price=2352.30,
        news=False,
    )

    trade = TradeSetup(
        symbol="XAUUSD",
        direction="BUY",
        entry=2352.30,
        stop_loss=2348.30,
        take_profit=2360.30,
        risk_percent=1.0,
        reward_ratio=2.0,
        confidence=0,
        status="Pending",
    )

    confidence = calculate_confidence(market)

    risk_ok = check_risk(trade)

    decision = make_decision(
        confidence,
        risk_ok,
        market.trend,
    )

    explanation = generate_explanation(
        decision=decision,
        confidence=confidence,
        trend=market.trend,
        session=market.session,
        risk_ok=risk_ok,
        news=market.news,
    )

    signal = generate_signal(
        symbol=trade.symbol,
        action=decision,
        entry=trade.entry,
        stop_loss=trade.stop_loss,
        take_profit=trade.take_profit,
        confidence=confidence,
        explanation=explanation,
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )

    print(signal)


if __name__ == "__main__":
    main()
