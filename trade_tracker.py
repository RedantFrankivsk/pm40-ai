# =========================
# PM40 TRADE TRACKER (FINAL HARD FIX v5)
# =========================

import json
import os
from datetime import datetime, timezone

from experience_logger import ExperienceLogger
from data_fetcher import get_candles
from atr_utils import calculate_atr
from risk_manager import RiskManager
from telegram_notifier import send_result

# 🔥 NEW
from pattern_memory import PatternMemory

FILE = "trades.json"

logger = ExperienceLogger()
risk = RiskManager()

# 🔥 NEW
pattern_memory = PatternMemory()


def now_utc():
    return datetime.now(timezone.utc)


def normalize_pattern(tf_features):
    try:
        return "|".join([
            f"{k}:{v.get('signal','')}_{v.get('structure','')}_{v.get('trend','')}"
            for k, v in sorted(tf_features.items())
        ])
    except:
        return str(tf_features)


# =========================
# LOAD / SAVE
# =========================
def load_trades():

    if not os.path.exists(FILE):
        with open(FILE, "w") as f:
            json.dump([], f)
        return []

    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []


def save_trades(trades):
    with open(FILE, "w") as f:
        json.dump(trades, f, indent=4)


# =========================
# ATR
# =========================
def get_atr(symbol):

    candles = get_candles(symbol, "15min")

    if not candles:
        return 0

    return calculate_atr(candles)


def dynamic_expiration(atr):

    if atr < 0.0005:
        return 10
    elif atr < 0.001:
        return 15
    else:
        return 20


# =========================
# REGISTER
# =========================
def register_trade(symbol, signal, entry_price, tf_features, confidence, expiration=None):

    allow, reason = risk.can_trade()

    if not allow:
        print(f"⛔ RISK BLOCK: {reason}")
        print("⚠️ BYPASS → learning mode")
    else:
        print(f"[RISK] OK: {reason}")

    trades = load_trades()

    atr = get_atr(symbol)

    if expiration is None:
        expiration = dynamic_expiration(atr)

    bet_size = risk.get_bet_size(confidence)

    trade = {
        "id": f"{symbol}_{now_utc().timestamp()}",
        "symbol": symbol,
        "signal": signal,
        "entry_price": entry_price,
        "status": "OPEN",
        "result": None,
        "open_time": now_utc().isoformat(),
        "expiration": expiration,
        "bet_size": bet_size,
        "confidence": confidence,
        "tf_features": tf_features
    }

    trades.append(trade)

    save_trades(trades)

    print(f"[TRADE OPENED] {symbol} BET={bet_size} CONF={confidence} EXP={expiration}m")
    print(f"[TOTAL OPEN TRADES] {len(trades)}")

    return True


# =========================
# UPDATE (🔥 MAIN FIX HERE)
# =========================
def update_trades():

    trades = load_trades()

    if not trades:
        print("[TRACKER] No trades in file")
        return []

    updated = []
    closed_results = []

    print(f"[TRACKER] Active trades: {len(trades)}")

    for t in trades:

        if t.get("status") != "OPEN":
            continue

        open_time = datetime.fromisoformat(t["open_time"])
        now = now_utc()

        minutes = (now - open_time).total_seconds() / 60

        if minutes < t.get("expiration", 15):
            updated.append(t)
            continue

        candles = get_candles(t["symbol"], "15min")

        if not candles:
            updated.append(t)
            continue

        price = float(candles[-1]["close"])

        if t["signal"] == "UP":
            result = "WIN" if price > t["entry_price"] else "LOSS"
        else:
            result = "WIN" if price < t["entry_price"] else "LOSS"

        t["status"] = "CLOSED"
        t["result"] = result

        print(f"[TRADE CLOSED] {t['symbol']} -> {result}")

        send_result(t["symbol"], result)

        risk.update_after_trade(result)

        # =========================
        # 🔥🔥🔥 REAL LEARNING FIX
        # =========================
        pattern = normalize_pattern(t["tf_features"])

        pattern_memory.update(
            pattern=pattern,
            result=result,
            signal=t["signal"]
        )

        # =========================

        logger.log_trade(
            symbol=t["symbol"],
            signal=t["signal"],
            result=result,
            pattern=pattern,
            strategy_pattern=t["signal"],
            regime="default"
        )

        closed_results.append(result)

    save_trades(updated)

    return closed_results