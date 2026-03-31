# entry_logic.py

def check_entry(results, final_signal, confidence):
    if final_signal == "NEUTRAL":
        return {"entry": False, "reason": "no_signal"}

    # 🔥 адаптивний + агресивніший поріг
    if confidence >= 60:
        threshold = 55
    else:
        threshold = 45

    if confidence < threshold:
        return {"entry": False, "reason": "low_confidence"}

    trends = [r["signal"] for r in results]
    scores = [r["score"] for r in results]

    # --- TREND ENTRY ---
    if trends.count(final_signal) >= 2:
        return {"entry": True, "reason": "pullback_trend"}

    # 🔥 WEAK TREND BUILDING
    if sum(scores) > 1.5:
        return {"entry": True, "reason": "weak_trend_building"}

    # 🔥 TF CONFLICT → REVERSAL
    if len(scores) >= 2 and scores[0] * scores[1] < 0:
        return {"entry": True, "reason": "tf_conflict_reversal"}

    return {"entry": False, "reason": "no_setup"}