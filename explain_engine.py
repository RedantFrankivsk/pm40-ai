def explain_signal(signal, pstats, risk):
    reasons = []

    if pstats["trend"] != "flat":
        reasons.append(f"Тренд: {pstats['trend']}")
    else:
        reasons.append("Ринок у флеті")

    if pstats["volume"] == "growing":
        reasons.append("Обʼєм зростає")
    elif pstats["volume"] == "falling":
        reasons.append("Обʼєм падає")

    if pstats["structure"] == "breakout":
        reasons.append("Є пробій структури")
    else:
        reasons.append("Ціна в діапазоні")

    if pstats["memory_hits"] > 0:
        reasons.append(f"Патерн знайдений у памʼяті ({pstats['memory_hits']})")
    else:
        reasons.append("Новий патерн (без історії)")

    reasons.append(f"Ризик: {risk}")

    return "; ".join(reasons)
