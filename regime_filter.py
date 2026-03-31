# regime_filter.py

def apply_regime_filter(decision, confidence, entropy, regime):
    """
    Regime-aware confidence adjustment.
    Returns (decision, adjusted_confidence)
    """

    adj_conf = confidence

    # CHAOS: ріжемо впевненість + можливий NEUTRAL
    if regime == "CHAOS":
        adj_conf *= 0.55

        # якщо шум зашкалює — гасимо сигнал
        if entropy >= 1.3 and abs(adj_conf) < 0.6:
            return "NEUTRAL", 0.0

    # TRANSITION: легке згладжування
    elif regime == "TRANSITION":
        adj_conf *= 0.8

    # TREND: підсилення
    elif regime == "TREND":
        adj_conf *= 1.15

    # кліпінг
    adj_conf = max(min(adj_conf, 1.0), -1.0)

    # якщо впевненість замала — нейтраль
    if abs(adj_conf) < 0.25:
        return "NEUTRAL", adj_conf

    return decision, adj_conf
