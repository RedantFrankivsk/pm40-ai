# signal_consistency.py
import time

class SignalConsistency:
    def __init__(self):
        self.last = {}

    def check(self, key, new_signal):
        """
        key = symbol|tf
        new_signal = dict from decision_engine
        """
        now = time.time()

        prev = self.last.get(key)
        if not prev:
            self.last[key] = {
                "signal": new_signal["signal"],
                "confidence": new_signal["confidence"],
                "stage": new_signal["pattern_stage"],
                "regime": new_signal["market_regime"],
                "ts": now
            }
            return new_signal

        # --- cooldown ---
        if now - prev["ts"] < 180:
            return prev | {"locked": True}

        # --- regime changed ---
        if new_signal["market_regime"] != prev["regime"]:
            self._update(key, new_signal, now)
            return new_signal | {"reason": "REGIME_CHANGE"}

        # --- stage changed ---
        if new_signal["pattern_stage"] != prev["stage"]:
            self._update(key, new_signal, now)
            return new_signal | {"reason": "STAGE_CHANGE"}

        # --- confidence delta ---
        delta = abs(new_signal["confidence"] - prev["confidence"])
        if delta >= 12:
            self._update(key, new_signal, now)
            return new_signal | {"reason": "CONF_DELTA"}

        # --- otherwise lock ---
        return prev | {"locked": True}

    def _update(self, key, signal, now):
        self.last[key] = {
            "signal": signal["signal"],
            "confidence": signal["confidence"],
            "stage": signal["pattern_stage"],
            "regime": signal["market_regime"],
            "ts": now
        }
