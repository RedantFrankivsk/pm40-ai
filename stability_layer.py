# stability_layer.py
import time

MAX_AUTHORITY = 5.0
MIN_AUTHORITY = -3.0

COOLDOWN_AFTER_WIN = 2
COOLDOWN_AFTER_LOSS = 5

_last_trade_time = 0
_last_result = None


def apply_stability(engine_result: dict) -> dict:
    global _last_trade_time, _last_result

    now = time.time()

    if _last_result == "WIN" and now - _last_trade_time < COOLDOWN_AFTER_WIN:
        engine_result["meta"] = {"allow_trade": False, "reason": "COOLDOWN_AFTER_WIN"}
        return engine_result

    if _last_result == "LOSS" and now - _last_trade_time < COOLDOWN_AFTER_LOSS:
        engine_result["meta"] = {"allow_trade": False, "reason": "COOLDOWN_AFTER_LOSS"}
        return engine_result

    authority = engine_result.get("authority", 0)
    authority = max(MIN_AUTHORITY, min(MAX_AUTHORITY, authority))
    engine_result["authority"] = round(authority, 2)

    return engine_result


def register_stability_result(result: str):
    global _last_trade_time, _last_result
    _last_trade_time = time.time()
    _last_result = result
