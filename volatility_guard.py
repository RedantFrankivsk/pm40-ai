import time
from collections import deque, defaultdict


class VolatilityGuard:
    def __init__(self, window=12, chaos_threshold=0.55):
        self.window = window
        self.chaos_threshold = chaos_threshold
        self.history = defaultdict(lambda: deque(maxlen=window))

    def register(self, tf: str, session: str, confidence: int, signal: str):
        key = f"{tf}|{session}"
        self.history[key].append({
            "confidence": confidence,
            "signal": signal,
            "ts": time.time()
        })

    def is_chaos(self, tf: str, session: str) -> bool:
        key = f"{tf}|{session}"
        data = self.history.get(key)

        if not data or len(data) < self.window:
            return False

        # частота зміни сигналів
        flips = 0
        last = None
        for d in data:
            if last and d["signal"] != last:
                flips += 1
            last = d["signal"]

        flip_ratio = flips / len(data)

        # середня впевненість
        avg_conf = sum(d["confidence"] for d in data) / len(data)

        chaos_score = (flip_ratio * 0.6) + ((50 - avg_conf) / 50 * 0.4)

        return chaos_score >= self.chaos_threshold


# singleton
volatility_guard = VolatilityGuard()
