# =========================
# PATTERN MEMORY V8 (STABLE KEY FIX)
# =========================

import json
import os
from datetime import datetime, timedelta

FILE = "pattern_memory.json"

DECAY_DAYS = 7
MIN_TRADES = 5
MAX_TRADES_PER_PATTERN = 50


def load_patterns():
    if not os.path.exists(FILE):
        return {}

    try:
        with open(FILE, "r") as f:
            data = json.load(f)
            if not isinstance(data, dict):
                return {}
            return data
    except:
        return {}


def save_patterns(data):
    try:
        with open(FILE, "w") as f:
            json.dump(data, f, indent=4)
    except:
        pass


def normalize_trade(t):

    if isinstance(t, str):
        return {
            "signal": "UNKNOWN",
            "result": t,
            "time": str(datetime.now())
        }

    if isinstance(t, dict):

        result = t.get("result", "LOSS")

        if result not in ["WIN", "LOSS"]:
            result = "LOSS"

        return {
            "signal": t.get("signal", "UNKNOWN"),
            "result": result,
            "time": t.get("time", str(datetime.now()))
        }

    return None


def is_fresh(trade_time_str):
    try:
        trade_time = datetime.fromisoformat(trade_time_str)
    except:
        return True

    return datetime.now() - trade_time <= timedelta(days=DECAY_DAYS)


class PatternMemory:

    def __init__(self):
        pass

    def get_pattern_stats(self, pattern):

        pattern = str(pattern)  # 🔥 FIX

        patterns = load_patterns()

        if pattern not in patterns:
            return {"trades": 0, "wins": 0, "winrate": 0.0}

        raw_trades = patterns[pattern]

        trades = []
        wins = 0

        for t in raw_trades:

            nt = normalize_trade(t)

            if not nt:
                continue

            if not is_fresh(nt["time"]):
                continue

            trades.append(nt)

            if nt["result"] == "WIN":
                wins += 1

        total = len(trades)

        if total == 0:
            return {"trades": 0, "wins": 0, "winrate": 0.0}

        return {
            "trades": total,
            "wins": wins,
            "winrate": round(wins / total, 3)
        }

    def all_patterns(self):
        return list(load_patterns().keys())

    def update(self, pattern, result, signal=None):

        pattern = str(pattern)  # 🔥 FIX

        if result not in ["WIN", "LOSS"]:
            return

        patterns = load_patterns()

        if pattern not in patterns:
            patterns[pattern] = []

        patterns[pattern].append({
            "signal": signal if signal else "UNKNOWN",
            "result": result,
            "time": str(datetime.now())
        })

        if len(patterns[pattern]) > MAX_TRADES_PER_PATTERN:
            patterns[pattern] = patterns[pattern][-MAX_TRADES_PER_PATTERN:]

        save_patterns(patterns)