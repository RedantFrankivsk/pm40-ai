from datetime import datetime, timezone

def detect_session():
    hour = datetime.now(timezone.utc).hour

    if 0 <= hour < 6:
        return "ASIA"
    elif 6 <= hour < 12:
        return "LONDON"
    elif 12 <= hour < 20:
        return "NEW_YORK"
    else:
        return "OFF"

SESSION_RULES = {
    "ASIA": {
        "risk_mul": 1.2,
        "conf_mul": 0.9,
        "note": "Low liquidity / fake moves"
    },
    "LONDON": {
        "risk_mul": 1.0,
        "conf_mul": 1.0,
        "note": "Impulse session"
    },
    "NEW_YORK": {
        "risk_mul": 0.85,
        "conf_mul": 1.05,
        "note": "High volatility"
    },
    "OFF": {
        "risk_mul": 1.3,
        "conf_mul": 0.8,
        "note": "Dead market"
    }
}
