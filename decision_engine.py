from statistics import mean


def get_signal(candles, debug=False):
    if not candles or len(candles) < 30:
        return _result("NEUTRAL", 0, "not_enough_data")

    closes = [float(c["close"]) for c in candles]
    highs = [float(c["high"]) for c in candles]
    lows = [float(c["low"]) for c in candles]
    volumes = [float(c.get("volume", 1)) for c in candles]

    trend = _analyze_trend(closes)
    structure = _analyze_structure(highs, lows, closes)
    volume = _analyze_volume(volumes)
    volatility = _analyze_volatility(highs, lows)

    score = 0

    # 🔥 TREND (сильніший)
    if trend == "UP":
        score += 2
    elif trend == "DOWN":
        score -= 2

    # 🔥 STRUCTURE
    if structure == "BREAKOUT_UP":
        score += 2
    elif structure == "BREAKOUT_DOWN":
        score -= 2

    # 🔥 ДОБАВЛЯЄМО: continuation логіку
    if structure == "RANGE":
        if trend == "UP":
            score += 0.5
        elif trend == "DOWN":
            score -= 0.5

    # 🔥 VOLUME
    if volume == "STRONG_BUY":
        score += 0.7
    elif volume == "STRONG_SELL":
        score -= 0.7

    # 🔥 VOLATILITY (менше душимо)
    if volatility == "LOW":
        score *= 0.95

    # 🔥 FIX: знижений поріг
    if score >= 0.7:
        signal = "UP"
    elif score <= -0.7:
        signal = "DOWN"
    else:
        signal = "NEUTRAL"

    return {
        "signal": signal,
        "score": round(score, 3),
    }


def get_final_decision(results):

    weights = [1, 2, 3]

    total_score = 0

    for i, r in enumerate(results):
        w = weights[i] if i < len(weights) else 1
        total_score += r["score"] * w

    # 🔥 FIX: нормальний confidence
    confidence = min(int(abs(total_score) * 15), 95)

    # 🔥 FIX: нижчий поріг
    if total_score > 0.8:
        return "UP", confidence
    elif total_score < -0.8:
        return "DOWN", confidence
    else:
        return "NEUTRAL", confidence


def _analyze_trend(closes):
    fast = mean(closes[-5:])
    slow = mean(closes[-20:])
    if fast > slow:
        return "UP"
    elif fast < slow:
        return "DOWN"
    return "FLAT"


def _analyze_structure(highs, lows, closes):
    recent_high = max(highs[-20:])
    recent_low = min(lows[-20:])
    current = closes[-1]

    if current > recent_high:
        return "BREAKOUT_UP"
    if current < recent_low:
        return "BREAKOUT_DOWN"

    return "RANGE"


def _analyze_volume(volumes):
    avg = mean(volumes[:-1])
    last = volumes[-1]

    if last > avg * 1.5:
        return "STRONG_BUY"
    elif last < avg * 0.5:
        return "STRONG_SELL"
    return "NORMAL"


def _analyze_volatility(highs, lows):
    ranges = [h - l for h, l in zip(highs[-14:], lows[-14:])]
    avg = mean(ranges)
    if ranges[-1] < avg * 0.5:
        return "LOW"
    return "NORMAL"


def _result(signal, score, reason):
    return {
        "signal": signal,
        "score": score,
        "details": {"reason": reason}
    }