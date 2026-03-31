# volume_analyzer.py

def analyze_volume(candles):
    """
    Аналіз об'єму:
    NORMAL / STRONG_BUY / STRONG_SELL
    """

    if len(candles) < 20:
        return "NORMAL"

    volumes = [float(c.get("volume", 0)) for c in candles]

    avg_volume = sum(volumes[-20:]) / 20
    last_volume = volumes[-1]

    last = candles[-1]
    prev = candles[-2]

    last_close = float(last["close"])
    prev_close = float(prev["close"])

    # --- базова логіка ---
    if last_volume > avg_volume * 1.5:
        if last_close > prev_close:
            return "STRONG_BUY"
        elif last_close < prev_close:
            return "STRONG_SELL"

    return "NORMAL"