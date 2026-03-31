def detect_structure(candles):

    if len(candles) < 30:
        return {
            "trend": "NEUTRAL",
            "structure": "RANGE",
            "score": 0
        }

    closes = [float(c["close"]) for c in candles]

    sma_fast = sum(closes[-10:]) / 10
    sma_slow = sum(closes[-30:]) / 30

    if sma_fast > sma_slow:
        trend = "UP"
    elif sma_fast < sma_slow:
        trend = "DOWN"
    else:
        trend = "NEUTRAL"

    last = closes[-1]
    prev = closes[-2]

    if trend == "UP":
        structure = "PULLBACK" if last < prev else "TREND"
    elif trend == "DOWN":
        structure = "PULLBACK" if last > prev else "TREND"
    else:
        structure = "RANGE"

    score = 0

    if trend == "UP":
        score += 2
    elif trend == "DOWN":
        score -= 2

    if structure == "TREND":
        score += 1 if trend == "UP" else -1

    return {
        "trend": trend,
        "structure": structure,
        "score": score
    }