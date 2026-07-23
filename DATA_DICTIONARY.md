# GTI AI Data Dictionary

## Market Context

| Field | Type | Description |
|-------|------|-------------|
| symbol | string | Trading symbol |
| trend | string | Bullish/Bearish/Sideways |
| timeframe | string | H4, H1, M15 |
| session | string | Asia, London, New York |
| news | bool | High-impact news |

---

## Trade Setup

| Field | Type | Description |
|-------|------|-------------|
| direction | string | BUY or SELL |
| entry | float | Entry price |
| stop_loss | float | Stop Loss |
| take_profit | float | Take Profit |
| risk_reward | float | Risk Reward ratio |

---

## Decision

| Field | Type | Description |
|-------|------|-------------|
| decision | string | BUY / SELL / WAIT / NO TRADE |
| confidence | int | 0–100 |
| explanation | string | Why this decision was made |

---

## Journal

| Field | Type | Description |
|-------|------|-------------|
| result | string | Win / Loss / Breakeven |
| profit_loss | float | P/L |
| lesson | string | Lesson learned |
