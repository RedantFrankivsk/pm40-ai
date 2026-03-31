def analyze_structure(description: str):
    desc = description.lower()

    # базові прапори
    hh = "higher high" in desc or "hh" in desc
    hl = "higher low" in desc or "hl" in desc
    lh = "lower high" in desc or "lh" in desc
    ll = "lower low" in desc or "ll" in desc

    breakout = "пробой" in desc or "breakout" in desc
    range_words = ["флет", "range", "боковик", "нет направления"]

    # FLAT
    if any(w in desc for w in range_words):
        return {
            "structure": "RANGE",
            "bias": "NEUTRAL",
            "confidence_bonus": -10,
            "explain": "Ринок у діапазоні"
        }

    # UP STRUCTURE
    if (hh and hl) or (hl and breakout):
        return {
            "structure": "TREND",
            "bias": "UP",
            "confidence_bonus": 10,
            "explain": "Структура HH/HL"
        }

    # DOWN STRUCTURE
    if (ll and lh) or (lh and breakout):
        return {
            "structure": "TREND",
            "bias": "DOWN",
            "confidence_bonus": 10,
            "explain": "Структура LH/LL"
        }

    # НЕВИЗНАЧЕНО
    return {
        "structure": "UNCLEAR",
        "bias": "NEUTRAL",
        "confidence_bonus": 0,
        "explain": "Структура неочевидна"
    }
