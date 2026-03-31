# =========================
# PM40 REGIME ENGINE (SMART FIX)
# =========================

def safe_get(d, key, default):
    return d[key] if key in d else default


def detect_regime(tf_features):

    h1 = tf_features["H1"]
    m30 = tf_features["M30"]
    m15 = tf_features["M15"]

    trend_h1 = safe_get(h1, "trend", "FLAT")
    trend_m30 = safe_get(m30, "trend", "FLAT")
    trend_m15 = safe_get(m15, "trend", "FLAT")

    print(f"[REGIME INPUT] H1={trend_h1} M30={trend_m30} M15={trend_m15}")

    trends = [trend_h1, trend_m30, trend_m15]

    up_count = trends.count("UP")
    down_count = trends.count("DOWN")

    # 🔥 2 з 3 вже тренд
    if up_count >= 2:
        return "TREND"

    if down_count >= 2:
        return "TREND"

    # 🔥 якщо всі різні → хаос
    if len(set(trends)) == 3:
        return "CHAOS"

    return "RANGE"


def apply_regime_filter(signal, confidence, regime):

    if regime == "CHAOS":
        confidence *= 0.6

    elif regime == "RANGE":
        confidence *= 0.8

    elif regime == "TREND":
        confidence *= 1.2

    confidence = max(0, min(100, confidence))

    if confidence < 30:
        return "NEUTRAL", confidence

    return signal, confidence


def apply_regime_pressure(signal, confidence, regime):

    if regime == "TREND":
        confidence += 5

    elif regime == "CHAOS":
        confidence -= 10

    return max(0, min(100, confidence))


def build_regime(tf_features):
    return detect_regime(tf_features)