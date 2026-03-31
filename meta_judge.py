def judge(engine_result: dict) -> dict:
    decision = {
        "allow_trade": True,
        "reason": "OK",
        "adjusted_risk": engine_result.get("risk", 0.1),
        "meta_score": 1.0,
        "notes": []
    }

    if engine_result["signal"] == "NEUTRAL":
        decision["allow_trade"] = False
        decision["reason"] = "NEUTRAL_SIGNAL"
        decision["meta_score"] = 0.0
        return decision

    if engine_result.get("borrowed") and not engine_result.get("trusted"):
        decision["allow_trade"] = False
        decision["reason"] = "BORROWED_NOT_TRUSTED"
        decision["meta_score"] = -0.5
        decision["adjusted_risk"] *= 0.4
        return decision

    if engine_result.get("trusted"):
        decision["meta_score"] += 0.4
        decision["notes"].append("Trusted pattern")

    if engine_result.get("anti_luck"):
        decision["adjusted_risk"] *= 0.7
        decision["notes"].append("Anti-luck applied")

    return decision
