
# =========================
# EXPIRATION ENGINE
# =========================

def get_expiration(tf_features, confidence):
    m15 = tf_features["M15"]
    m30 = tf_features["M30"]

    # ===== STRONG TREND =====
    if (
        "breakout" in m15["structure"]
        and m30["trend"] == m15["trend"]
        and confidence >= 70
    ):
        return 15

    # ===== NORMAL SETUP =====
    if m15["structure"] == "pullback":
        return 20

    # ===== WEAK =====
    return 30