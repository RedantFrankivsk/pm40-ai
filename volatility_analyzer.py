# volatility_analyzer.py

def analyze_volatility(candles):
    """
    LOW / NORMAL / HIGH волатильність
    """

    if len(candles) < 20:
        return "NORMAL"

    ranges = []

    for c in candles[-20:]:
        high = float(c["high"])
        low = float(c["low"])
        ranges.append(high - low)

    avg_range = sum(ranges) / len(ranges)
    last_range = ranges[-1]

    # --- логіка ---
    if last_range > avg_range * 1.5:
        return "HIGH"

    elif last_range < avg_range * 0.7:
        return "LOW"

    return "NORMAL"