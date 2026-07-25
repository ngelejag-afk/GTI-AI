"""
GTI AI
Main Application
Version 4.0
"""

from broker.demo_broker import DemoBroker
from broker.order_engine import OrderEngine
from broker.portfolio_engine import PortfolioEngine
from broker.trade_executor import TradeExecutor
from broker.trade_manager import TradeManager
from config.settings import Settings
from core.risk_manager import RiskManager
from core.trading_engine import TradingEngine
from data.data_provider import DataProvider
from data.demo_data_source import DemoDataSource
from strategy.strategy_engine import StrategyEngine
from strategy.trend_strategy import TrendStrategy


def main() -> None:
    """
    Run the GTI AI trading pipeline.
    """

    data_source = DemoDataSource()
    provider = DataProvider(data_source)

    history = provider.history(
        symbol=Settings.SYMBOL,
        timeframe=Settings.TIMEFRAME,
        candles=Settings.HISTORY_CANDLES,
    )

    strategy = TrendStrategy(
        history=history,
        symbol=Settings.SYMBOL,
    )

    order = StrategyEngine(strategy).analyze()

    if order is None:
        print("No trade setup found.")
        return

    broker = DemoBroker()
    broker.connect()

    portfolio = PortfolioEngine()
    trade_manager = TradeManager()
    risk_manager = RiskManager(
        portfolio=portfolio,
        trade_manager=trade_manager,
    )

    order_engine = OrderEngine()
    executor = TradeExecutor(
        broker=broker,
        order_engine=order_engine,
    )

    trading_engine = TradingEngine(
        executor=executor,
        risk_manager=risk_manager,
    )

    if trading_engine.execute(order):
        print("Trade executed successfully.")
        print(order)
    else:
        print("Trade execution rejected.")


if __name__ == "__main__":
    main()
