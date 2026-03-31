# pattern_engine.py

from context_engine import detect_volatility
from context_engine import detect_session
from context_engine import detect_trend_strength


def build_pattern(
    trend_15m,
    trend_30m,
    trend_1h,
    structure,
    volume,
    market_regime,
    atr,
    price,
    hour,
    trend_score
):

    tokens = []

    # timeframe trends
    tokens.append(f"15m_{trend_15m}")
    tokens.append(f"30m_{trend_30m}")
    tokens.append(f"1h_{trend_1h}")

    # structure
    tokens.append(structure)

    # volume
    tokens.append(volume)

    # market regime
    tokens.append(market_regime)

    # context features
    volatility = detect_volatility(atr, price)
    session = detect_session(hour)
    trend_strength = detect_trend_strength(trend_score)

    tokens.append(volatility)
    tokens.append(session)
    tokens.append(trend_strength)

    return " ".join(tokens)