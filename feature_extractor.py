import statistics

# =========================
# HELPERS
# =========================

def get_closes(candles):
    return [c["close"] for c in candles]

def get_volumes(candles):
    return [c["volume"] for c in candles]


# =========================
# TREND
# =========================

def detect_trend(candles):
    closes = get_closes(candles)

    if len(closes) < 20:
        return "unknown"

    sma_short = sum(closes[-10:]) / 10
    sma_long = sum(closes[-20:]) / 20

    if sma_short > sma_long:
        return "up"
    elif sma_short < sma_long:
        return "down"
    else:
        return "flat"


# =========================
# VOLUME
# =========================

def detect_volume(candles):
    volumes = get_volumes(candles)

    if len(volumes) < 20:
        return "unknown"

    avg_volume = sum(volumes[-20:]) / 20
    current_volume = volumes[-1]

    if current_volume > avg_volume * 1.2:
        return "high"
    elif current_volume < avg_volume * 0.8:
        return "low"
    else:
        return "normal"


# =========================
# VOLATILITY
# =========================

def detect_volatility(candles):
    closes = get_closes(candles)

    if len(closes) < 20:
        return "unknown"

    returns = []

    for i in range(1, len(closes)):
        returns.append(abs(closes[i] - closes[i-1]))

    avg_vol = sum(returns[-20:]) / 20
    current_vol = returns[-1]

    if current_vol > avg_vol * 1.3:
        return "high"
    elif current_vol < avg_vol * 0.7:
        return "low"
    else:
        return "normal"


# =========================
# STRUCTURE
# =========================

def detect_structure(candles):
    if len(candles) < 10:
        return "unknown"

    last = candles[-1]
    prev = candles[-2]

    # простий патерн
    if last["close"] > prev["high"]:
        return "breakout_up"

    if last["close"] < prev["low"]:
        return "breakout_down"

    # pullback (дуже грубо)
    closes = get_closes(candles)

    if closes[-1] < max(closes[-5:]):
        return "pullback"

    return "range"


# =========================
# MAIN FEATURE EXTRACTOR
# =========================

def extract_features(candles):
    return {
        "trend": detect_trend(candles),
        "volume": detect_volume(candles),
        "volatility": detect_volatility(candles),
        "structure": detect_structure(candles)
    }


# =========================
# TEST
# =========================

if __name__ == "__main__":
    from market_data_engine import load_market_data

    print("=== FEATURE EXTRACTOR TEST ===")

    data = load_market_data()

    for pair in data:
        print(f"\nPAIR: {pair}")

        for tf in data[pair]:
            features = extract_features(data[pair][tf])
            print(f"{tf}: {features}")