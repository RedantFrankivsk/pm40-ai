def htf_bias(htf_description: str):
    d = htf_description.lower()

    if "флет" in d or "range" in d or "нет направления" in d:
        return {
            "bias": "NEUTRAL",
            "bonus": -5,
            "explain": "HTF: флет"
        }

    if "восход" in d or "higher high" in d or "up" in d:
        return {
            "bias": "UP",
            "bonus": 10,
            "explain": "HTF: восходящий тренд"
        }

    if "нисход" in d or "lower low" in d or "down" in d:
        return {
            "bias": "DOWN",
            "bonus": 10,
            "explain": "HTF: нисходящий тренд"
        }

    return {
        "bias": "NEUTRAL",
        "bonus": 0,
        "explain": "HTF: не определён"
    }
