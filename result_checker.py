
# =========================
# RESULT CHECKER (FINAL FIXED)
# =========================

from datetime import datetime, timedelta

from trade_memory import get_open_trades, update_trade_result
from pattern_memory import update_pattern


def check_results(data):
    print("\n=== CHECKING TRADE RESULTS ===")

    trades = get_open_trades()

    if not trades:
        print("No open trades")
        return

    for trade in trades:
        trade_time = datetime.fromisoformat(trade["time"])
        expire_time = trade_time + timedelta(minutes=trade["expiration"])

        if datetime.now() < expire_time:
            continue

        symbol = trade["symbol"]
        signal = trade["signal"]
        entry_price = trade["entry_price"]

        try:
            last_price = data[symbol]["M15"][-1]["close"]
        except:
            print(f"[SKIP] No data for {symbol}")
            continue

        if signal == "BUY":
            result = "WIN" if last_price > entry_price else "LOSS"
        elif signal == "SELL":
            result = "WIN" if last_price < entry_price else "LOSS"
        else:
            continue

        update_trade_result(trade["id"], result)
        update_pattern(trade["tf_features"], result)

        print(f"{symbol} → {result}")