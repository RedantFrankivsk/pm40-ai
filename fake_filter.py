# fake_filter.py

def is_fake_move(tf_features, direction):
    """
    Повертає True якщо рух підозрілий (НЕ входити)
    """

    fake_signals = 0

    for tf in tf_features:
        f = tf_features[tf]

        structure = f.get("structure")
        volume = f.get("volume")
        volatility = f.get("volatility")
        trend = f.get("trend")

        # =========================
        # 1. WEAK BREAKOUT
        # =========================
        if structure in ["BREAKOUT_UP", "BREAKOUT_DOWN"]:
            if volume != "STRONG_BUY" and volume != "STRONG_SELL":
                fake_signals += 1

        # =========================
        # 2. LOW VOLATILITY MOVE
        # =========================
        if volatility == "LOW":
            fake_signals += 1

        # =========================
        # 3. TREND CONFLICT
        # =========================
        if structure == "PULLBACK":
            if trend != direction:
                fake_signals += 1

    # =========================
    # FINAL DECISION
    # =========================
    if fake_signals >= 2:
        return True

    return False