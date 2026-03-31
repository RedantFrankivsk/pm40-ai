# regime_pressure.py
# v9.4 — Regime pressure model

def apply_regime_pressure(
    signal: str,
    confidence: float,
    regime: str
) -> float:

    regime = regime.upper()

    if regime == "TREND":
        if signal in ("UP", "DOWN"):
            confidence += 0.1
        else:
            confidence -= 0.1

    if regime == "RANGE":
        if signal in ("UP", "DOWN"):
            confidence -= 0.2
        else:
            confidence += 0.1

    return round(max(0.0, min(1.0, confidence)), 2)
