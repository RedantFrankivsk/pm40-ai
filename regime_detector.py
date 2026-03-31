
# =========================
# PM40 REGIME DETECTOR (FINAL)
# =========================

def detect_regime(tf_features):
    """
    Визначає режим ринку:
    TREND / RANGE / CHAOS
    """

    h1 = tf_features["H1"]
    m30 = tf_features["M30"]
    m15 = tf_features["M15"]

    trend_h1 = h1["trend"]
    trend_m30 = m30["trend"]
    trend_m15 = m15["trend"]

    vol_h1 = h1["volatility"]
    vol_m30 = m30["volatility"]
    vol_m15 = m15["volatility"]

    structure_m15 = m15["structure"]
    structure_m30 = m30["structure"]

    # =========================
    # 1. CHAOS (пріоритет)
    # =========================
    # різні тренди між TF
    if not (trend_h1 == trend_m30 == trend_m15):
        return "CHAOS"

    # різкий breakout + шум
    if vol_m15 == "high" and structure_m15 in ["breakout_up", "breakout_down"]:
        if vol_h1 == "low":
            return "CHAOS"

    # =========================
    # 2. TREND
    # =========================
    if trend_h1 == trend_m30 == trend_m15:

        # breakout або нормальний рух
        if structure_m30 in ["breakout_up", "breakout_down", "pullback"]:

            # не слабкий ринок
            if vol_h1 != "low":
                return "TREND"

    # =========================
    # 3. RANGE
    # =========================
    # слабка волатильність
    if vol_h1 == "low" and vol_m30 == "low":
        return "RANGE"

    # багато pullback = флет
    if structure_m15 == "pullback" and structure_m30 == "pullback":
        return "RANGE"

    # =========================
    # DEFAULT
    # =========================
    return "CHAOS"
