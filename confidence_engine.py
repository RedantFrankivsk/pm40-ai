# =========================
# CONFIDENCE ENGINE V2 (UPGRADE)
# =========================

from pattern_memory import get_pattern_stats


# =========================
# MAIN FUNCTION
# =========================
def get_final_confidence(tf_signals, tf_features, tf_scores):
    """
    tf_signals: {
        "M15": "UP",
        "M30": "DOWN",
        "H1": "UP"
    }

    tf_features: {
        "M15": {"trend": "...", "structure": "...", "volatility": "..."},
        ...
    }

    tf_scores: {
        "M15": 2,
        "M30": -2,
        "H1": 2
    }
    """

    confidence = 50  # база

    # =========================
    # 1. TF ALIGNMENT (UPGRADE)
    # =========================
    directions = list(tf_signals.values())

    up_count = directions.count("UP")
    down_count = directions.count("DOWN")

    if up_count == 3 or down_count == 3:
        confidence += 25

    elif up_count == 2 or down_count == 2:
        confidence += 10

    elif "UP" in directions and "DOWN" in directions:
        confidence -= 15

    # =========================
    # 2. SCORE STRENGTH (NEW)
    # =========================
    total_strength = sum(abs(s) for s in tf_scores.values())

    if total_strength >= 5:
        confidence += 10
    elif total_strength <= 2:
        confidence -= 10

    # =========================
    # 3. STRUCTURE BOOST (FIXED)
    # =========================
    for tf in tf_features:
        structure = tf_features[tf].get("structure", "")

        if structure == "BULLISH":
            confidence += 3
        elif structure == "BEARISH":
            confidence += 3
        elif structure == "RANGE":
            confidence -= 2

    # =========================
    # 4. VOLATILITY FILTER (FIXED)
    # =========================
    low_vol_count = 0

    for tf in tf_features:
        if tf_features[tf].get("volatility") == "LOW":
            low_vol_count += 1

    if low_vol_count >= 2:
        confidence -= 15

    # =========================
    # 5. HTF PRIORITY (NEW)
    # =========================
    h1_signal = tf_signals.get("H1")
    m15_signal = tf_signals.get("M15")

    if h1_signal == m15_signal:
        confidence += 10
    else:
        confidence -= 5

    # =========================
    # 6. PATTERN MEMORY (SAFE)
    # =========================
    try:
        pattern_score = get_pattern_stats(tf_features)

        if pattern_score > 60:
            confidence += 10
        elif pattern_score < 40:
            confidence -= 10

    except Exception:
        pass  # щоб не ламало систему

    # =========================
    # 7. CLAMP
    # =========================
    confidence = max(0, min(100, confidence))

    return confidence