# =========================
# SIGNAL FILTER (PM40)
# =========================

def filter_signal(tf_signals, tf_features):
    """
    tf_signals = {
        "M15": "UP",
        "M30": "DOWN",
        "H1": "DOWN"
    }

    tf_features = {
        "M15": {...},
        "M30": {...},
        "H1": {...}
    }
    """

    h1 = tf_signals.get("H1")
    m30 = tf_signals.get("M30")
    m15 = tf_signals.get("M15")

    m15_structure = tf_features["M15"]["structure"]

    # =========================
    # BUY LOGIC
    # =========================
    if h1 == "UP" and m30 == "UP":
        if m15 == "UP" or m15_structure == "pullback":
            return "BUY"

    # =========================
    # SELL LOGIC
    # =========================
    if h1 == "DOWN" and m30 == "DOWN":
        if m15 == "DOWN" or m15_structure == "pullback":
            return "SELL"

    return "NO TRADE"


# =========================
# TEST
# =========================

if __name__ == "__main__":
    test_signals = {
        "M15": "UP",
        "M30": "DOWN",
        "H1": "DOWN"
    }

    test_features = {
        "M15": {"structure": "pullback"},
        "M30": {},
        "H1": {}
    }

    result = filter_signal(test_signals, test_features)
    print("Filtered:", result)