"""
GTI AI
Main Application Entry Point
"""

from datetime import datetime

from models.market import MarketContext
from models.trade import TradeSetup
from models.decision import Decision
from core.confidence_engine import calculate_confidence
from core.risk_engine import check_risk
from core.decision_engine import make_decision
from core.signal_engine import generate_signal


def main() -> None:
    market = MarketContext(
        symbol="XAUUSD",
        timeframe="H1",
        trend="Bullish",
        session="London",
        market_structure="Uptrend",
        key_level=3350.00,
        current_price=3352.50,
        news=False,
    )

    trade = TradeSetup(
        entry=3352.50,
        stop_loss=3348.50,
        take_profit=3360.50,
        risk_percent=1.0,
    )

    confidence = calculate_confidence(market)
    risk_ok = check_risk(trade)
    decision = make_decision(confidence, risk_ok)
    signal = generate_signal(decision)

    print("=" * 50)
    print("GTI AI")
    print("Gonline Trading Intelligence AI")
    print("=" * 50)
    print(f"Time       : {datetime.now()}")
    print(f"Symbol     : {market.symbol}")
    print(f"Trend      : {market.trend}")
    print(f"Session    : {market.session}")
    print(f"Confidence : {signal.confidence}%")
    print(f"Decision   : {signal.action}")
    print(f"Reason     : {signal.reason}")
    print("=" * 50)


if __name__ == "__main__":
    main()
