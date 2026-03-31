# liquidity_grab_detector.py

def detect_liquidity_grab(candles):
    if not candles or len(candles) < 20:
        return {"liquidity_grab": False}

    highs = [float(c["high"]) for c in candles]
    lows = [float(c["low"]) for c in candles]
    closes = [float(c["close"]) for c in candles]

    recent_high = max(highs[-10:-1])
    recent_low = min(lows[-10:-1])

    last_high = highs[-1]
    last_low = lows[-1]
    last_close = closes[-1]

    # 🔥 FAKE BREAKOUT UP (забрали ліквідність зверху)
    if last_high > recent_high and last_close < recent_high:
        return {
            "liquidity_grab": True,
            "type": "grab_up"
        }

    # 🔥 FAKE BREAKOUT DOWN (забрали ліквідність знизу)
    if last_low < recent_low and last_close > recent_low:
        return {
            "liquidity_grab": True,
            "type": "grab_down"
        }

    return {"liquidity_grab": False}