def detect_market_regime(description: str):
    d = description.lower()

    if "флет" in d or "range" in d or "боковик" in d:
        return "RANGE"

    if (
        "восходящий тренд" in d
        or "нисходящий тренд" in d
        or "пробой" in d
        or "импульс" in d
    ):
        return "TREND"

    if (
        "резкий" in d
        or "хаос" in d
        or "шум" in d
        or "рывки" in d
    ):
        return "CHAOS"

    return "UNKNOWN"
