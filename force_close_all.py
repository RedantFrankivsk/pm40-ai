# force_close_all.py

from trade_tracker import load_trades, save_trades, close_trade
from datetime import datetime

def force_close_all():
    trades = load_trades()

    if not trades:
        print("✅ Немає відкритих угод")
        return

    print(f"⚠️ Закриваємо {len(trades)} угод...\n")

    closed = []

    for trade in trades:
        try:
            result = close_trade(trade)
            closed.append(result)

            print(f"❌ CLOSED {trade['symbol']} | result={result.get('result', 0)}")

        except Exception as e:
            print(f"ERROR closing {trade['symbol']}: {e}")

    save_trades([])

    print("\n✅ ВСІ УГОДИ ЗАКРИТІ І ОЧИЩЕНІ")

if __name__ == "__main__":
    print("=== FORCE CLOSE ALL TRADES ===\n")
    force_close_all()