# fake_breakout_detector.py

def detect_fake_breakout(candles):
    """
    Виявляє фейковий пробій рівня
    """

    if len(candles) < 20:
        return {"fake_breakout": False}

    highs = [float(c["high"]) for c in candles[-20:]]
    lows = [float(c["low"]) for c in candles[-20:]]

    resistance = max(highs[:-3])
    support = min(lows[:-3])

    last = candles[-1]
    prev = candles[-2]

    last_close = float(last["close"])
    last_high = float(last["high"])
    last_low = float(last["low"])

    prev_close = float(prev["close"])

    # --- FAKE BREAKOUT UP ---
    fake_up = (
        last_high > resistance and
        last_close < resistance and
        prev_close > resistance
    )

    # --- FAKE BREAKOUT DOWN ---
    fake_down = (
        last_low < support and
        last_close > support and
        prev_close < support
    )

    if fake_up:
        return {
            "fake_breakout": True,
            "direction": "DOWN"
        }

    if fake_down:
        return {
            "fake_breakout": True,
            "direction": "UP"
        }

    return {"fake_breakout": False}