def session_bias(signal: str, session: str):
    session = session.upper()

    # базові правила
    rules = {
        "ASIA": {
            "UP": -5,
            "DOWN": -5,
            "NEUTRAL": 0,
            "explain": "Азія: низька волатильність"
        },
        "LONDON": {
            "UP": 10,
            "DOWN": 10,
            "NEUTRAL": -5,
            "explain": "Лондон: трендові рухи"
        },
        "NEW_YORK": {
            "UP": 8,
            "DOWN": 8,
            "NEUTRAL": -5,
            "explain": "NY: імпульси та пробої"
        }
    }

    if session not in rules:
        return {
            "bonus": 0,
            "risk_modifier": 1.0,
            "explain": "Невідома сесія"
        }

    bonus = rules[session].get(signal, 0)

    # ризик-корекція
    if session == "ASIA":
        risk_mod = 0.5
    elif session == "LONDON":
        risk_mod = 1.1
    else:
        risk_mod = 1.0

    return {
        "bonus": bonus,
        "risk_modifier": risk_mod,
        "explain": rules[session]["explain"]
    }
