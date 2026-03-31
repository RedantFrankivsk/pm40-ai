# context_engine.py

def detect_volatility(atr, price):

    if price is None or price == 0:
        return "volatility_unknown"

    if atr is None:
        return "volatility_unknown"

    ratio = atr / price

    if ratio < 0.001:
        return "volatility_low"

    if ratio > 0.003:
        return "volatility_high"

    return "volatility_normal"


def detect_session(hour):

    if 7 <= hour <= 11:
        return "session_london"

    if 13 <= hour <= 17:
        return "session_ny"

    return "session_asia"


def detect_trend_strength(score):

    if score >= 2:
        return "strong_trend"

    if score == 1:
        return "medium_trend"

    return "weak_trend"