# entry_engine.py

from fake_filter import is_fake_move


def get_entry(tf_signals, tf_features, confidence):

    # =========================
    # 0. CONFIDENCE FILTER
    # =========================
    if confidence < 60:
        return _no_entry("low_confidence")

    directions = list(tf_signals.values())

    up_count = directions.count("UP")
    down_count = directions.count("DOWN")

    # =========================
    # 1. DIRECTION
    # =========================
    if up_count >= 2:
        direction = "UP"
    elif down_count >= 2:
        direction = "DOWN"
    else:
        return _no_entry("no_alignment")

    # =========================
    # 2. BAD MARKET FILTER
    # =========================
    bad = 0

    for tf in tf_features:
        f = tf_features[tf]

        if f.get("structure") == "RANGE":
            bad += 1

        if f.get("volatility") == "LOW":
            bad += 1

    if bad >= 2:
        return _no_entry("bad_market")

    # =========================
    # 3. STRUCTURE CONFIRM
    # =========================
    strong_structure = False
    pullback_ok = True

    for tf in tf_features:
        s = tf_features[tf].get("structure")
        t = tf_features[tf].get("trend")

        if direction == "UP" and s in [
            "BREAKOUT_UP",
            "TREND_CONTINUATION_UP"
        ]:
            strong_structure = True

        if direction == "DOWN" and s in [
            "BREAKOUT_DOWN",
            "TREND_CONTINUATION_DOWN"
        ]:
            strong_structure = True

        if s == "PULLBACK":
            if t != direction:
                pullback_ok = False

    if strong_structure:
        entry_type = "BREAKOUT"

    elif pullback_ok:
        entry_type = "PULLBACK"

    else:
        return _no_entry("no_structure")

    # =========================
    # 4. FAKE FILTER (НОВЕ)
    # =========================
    if is_fake_move(tf_features, direction):
        return _no_entry("fake_move_detected")

    return {
        "entry": True,
        "direction": direction,
        "type": entry_type,
        "confidence": confidence
    }


def _no_entry(reason):
    return {
        "entry": False,
        "reason": reason
    }