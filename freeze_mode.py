import time
from collections import defaultdict, deque


class FreezeMode:
    def __init__(self, window=6, loss_threshold=0.6, freeze_minutes=30):
        self.window = window
        self.loss_threshold = loss_threshold
        self.freeze_minutes = freeze_minutes

        self.history = defaultdict(lambda: deque(maxlen=window))
        self.frozen_until = {}

    def register_result(self, tf: str, session: str, result: str):
        key = f"{tf}|{session}"
        self.history[key].append(result)

        losses = self.history[key].count("loss")
        ratio = losses / len(self.history[key])

        if ratio >= self.loss_threshold:
            self.frozen_until[key] = time.time() + self.freeze_minutes * 60

    def is_frozen(self, tf: str, session: str) -> bool:
        key = f"{tf}|{session}"
        until = self.frozen_until.get(key)

        if not until:
            return False

        if time.time() > until:
            del self.frozen_until[key]
            return False

        return True


# singleton
freeze_mode = FreezeMode()
