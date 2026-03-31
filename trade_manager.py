# trade_manager.py

from trade_tracker import load_trades


def is_trade_open(symbol):
    trades = load_trades()

    for t in trades:
        if t["symbol"] == symbol and t["status"] == "OPEN":
            return True

    return False


def can_open_trade(symbol):
    """
    Анти-спам:
    не відкривати новий трейд якщо вже є відкритий
    """
    if is_trade_open(symbol):
        print(f"⛔ SKIP: TRADE ALREADY OPEN ({symbol})")
        return False

    return True