# =========================
# PM40 FULL AI SYSTEM (FINAL ULTRA FIXED v8)
# =========================

import time
from datetime import datetime, UTC

from data_fetcher import get_candles
from decision_engine import get_signal, get_final_decision

from trade_tracker import register_trade, update_trades
from trade_manager import can_open_trade

from telegram_notifier import send_signal, get_chat_id

from regime_engine import (
    build_regime,
    apply_regime_filter,
    apply_regime_pressure
)

from pattern_pipeline import PatternPipeline
from committee_engine import CommitteeEngine
from self_learning_engine import SelfLearningEngine

from execution_optimizer import ExecutionOptimizer
from outcome_memory import OutcomeMemory

from structure_detector import detect_structure


CHAT_ID = get_chat_id()

SYMBOLS = [
    "EUR/USD",
    "GBP/USD",
    "USD/JPY",
    "AUD/USD",
    "USD/CAD"
]

TIMEFRAMES = ["15min", "30min", "1h"]

REQUEST_DELAY = 8
SYMBOL_DELAY = 5
CYCLE_SLEEP = 10


def get_expiration(tf_features):
    structure = tf_features["M15"]["structure"]

    if structure == "PULLBACK":
        return 15
    else:
        return 30


def is_market_open():
    now = datetime.now(UTC)
    return now.weekday() not in [5, 6]


def is_new_candle():
    now = datetime.now(UTC)
    return now.minute % 15 == 0


def safe_get_candles(symbol, tf):
    try:
        return get_candles(symbol, tf)
    except Exception as e:
        print(f"[FETCH ERROR] {symbol} {tf}: {e}")
        return []


def build_feature_block(candles, signal_data):

    structure = detect_structure(candles)

    return {
        "signal": signal_data.get("signal", "NEUTRAL"),
        "score": signal_data.get("score", 0),
        "trend": structure.get("trend", "FLAT"),
        "structure": structure.get("structure", "range"),
        "volatility": "normal"
    }


def get_default_feature():
    return {
        "signal": "NEUTRAL",
        "score": 0,
        "trend": "FLAT",
        "structure": "range",
        "volatility": "normal"
    }


def process_symbol(symbol, pattern_pipeline, committee, executor):

    print(f"\n🔍 {symbol}")

    results = []
    tf_features = {
        "M15": get_default_feature(),
        "M30": get_default_feature(),
        "H1": get_default_feature()
    }

    candles_m15 = None

    for tf in TIMEFRAMES:

        candles = safe_get_candles(symbol, tf)

        if not candles:
            results.append({"signal": "NEUTRAL", "score": 0})
            continue

        if tf == "15min":
            candles_m15 = candles

        signal_data = get_signal(candles)

        print(f"{tf}: {signal_data['signal']} {signal_data['score']}")

        feature_block = build_feature_block(candles, signal_data)

        results.append(signal_data)

        if tf == "15min":
            tf_features["M15"] = feature_block
        elif tf == "30min":
            tf_features["M30"] = feature_block
        elif tf == "1h":
            tf_features["H1"] = feature_block

        time.sleep(REQUEST_DELAY)

    if not candles_m15:
        return

    base_signal, confidence = get_final_decision(results)

    regime = build_regime(tf_features)

    print(f"[REGIME INPUT] {regime}")

    confidence = apply_regime_pressure(base_signal, confidence, regime)
    signal, confidence = apply_regime_filter(base_signal, confidence, regime)

    context = {
        "regime": regime,
        "hour": datetime.now(UTC).hour,
        "trend_score": confidence
    }

    pattern = pattern_pipeline.build(tf_features, context)
    decision = committee.decide(pattern, context, regime)

    signal = decision["signal"]
    confidence = decision["confidence"]

    print(f"🧠 {signal} {confidence}")

    if signal == "NEUTRAL":
        signal = base_signal

    if signal == "NEUTRAL":
        return

    if confidence <= 0:
        confidence = 0.2

    # =========================
    # 🔥 EXECUTION FILTER
    # =========================
    if not executor.should_execute(pattern, candles_m15, signal):
        print("🚫 BLOCKED (execution optimizer)")
        return

    # =========================
    # 🔥 RISK FILTER (HARD STOP)
    # =========================
    allowed = can_open_trade(symbol)

    if not allowed:
        print("🚫 BLOCKED BY RISK (NO BYPASS)")
        return  # ❗ ГОЛОВНИЙ ФІКС

    entry_price = float(candles_m15[-1]["close"])

    expiration = get_expiration(tf_features)

    opened = register_trade(
        symbol=symbol,
        signal=signal,
        entry_price=entry_price,
        tf_features=tf_features,
        confidence=confidence,
        expiration=expiration
    )

    if not opened:
        print("🚫 TRADE NOT OPENED")
        return

    print(f"🔥 ENTRY @ {entry_price}")

    try:
        send_signal(symbol, signal, confidence, True, expiration)
    except Exception as e:
        print(f"[TELEGRAM ERROR] {e}")


def run():

    print("=== PM40 FULL AI (FINAL ULTRA FIXED v8) ===\n")

    pattern_pipeline = PatternPipeline()
    committee = CommitteeEngine()
    self_learning = SelfLearningEngine()

    outcome_memory = OutcomeMemory()
    executor = ExecutionOptimizer(outcome_memory)

    last_candle_time = None

    while True:

        if not is_market_open():
            time.sleep(30)
            continue

        if not is_new_candle():
            time.sleep(CYCLE_SLEEP)
            continue

        now_key = datetime.now(UTC).strftime("%Y-%m-%d %H:%M")

        if now_key == last_candle_time:
            time.sleep(2)
            continue

        last_candle_time = now_key

        print(f"\n🚀 {now_key}\n")

        results = update_trades()

        if results:
            print(f"\n📊 CLOSED RESULTS: {results}\n")
        else:
            print("\n📊 NO CLOSED TRADES\n")

        for r in results:
            outcome_memory.update(r)

        for symbol in SYMBOLS:
            process_symbol(
                symbol,
                pattern_pipeline,
                committee,
                executor
            )
            time.sleep(SYMBOL_DELAY)

        print("\n--- NEXT ---\n")

        time.sleep(CYCLE_SLEEP)


if __name__ == "__main__":
    run()