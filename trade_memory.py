
# =========================
# PM40 TRADE MEMORY V4
# =========================

import json
import os
from datetime import datetime

MEMORY_FILE = "trade_memory.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []

    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=4)


def save_trade(symbol, signal, confidence, regime, expiration, entry_price, tf_features):
    memory = load_memory()

    trade = {
        "id": len(memory) + 1,
        "time": str(datetime.now()),
        "symbol": symbol,
        "signal": signal,
        "confidence": confidence,
        "regime": regime,
        "expiration": expiration,
        "entry_price": entry_price,
        "tf_features": tf_features,
        "result": None
    }

    memory.append(trade)
    save_memory(memory)

    print(f"[MEMORY] Trade saved #{trade['id']}")


def update_trade_result(trade_id, result):
    memory = load_memory()

    for trade in memory:
        if trade["id"] == trade_id:
            trade["result"] = result

    save_memory(memory)


def get_open_trades():
    memory = load_memory()
    return [t for t in memory if t["result"] is None]


def get_stats():
    memory = load_memory()

    wins = sum(1 for t in memory if t["result"] == "WIN")
    losses = sum(1 for t in memory if t["result"] == "LOSS")

    total = wins + losses
    winrate = round((wins / total) * 100, 2) if total > 0 else 0

    return {
        "wins": wins,
        "losses": losses,
        "winrate": winrate
    }