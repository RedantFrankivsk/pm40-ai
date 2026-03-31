# meta_guard.py
import json
import os
import time

FILE = "meta_guard.json"


class MetaGuard:
    def __init__(self):
        self.state = {}
        self._load()

    def _load(self):
        if os.path.exists(FILE):
            with open(FILE, "r", encoding="utf-8") as f:
                self.state = json.load(f)
        else:
            self.state = {}

    def _save(self):
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump(self.state, f, indent=2)

    def register(self, pid: str, outcome: str):
        now = time.time()

        if pid not in self.state:
            self.state[pid] = {
                "loss_streak": 0,
                "cooldown_until": 0
            }

        s = self.state[pid]

        if outcome == "LOSS":
            s["loss_streak"] += 1
        elif outcome == "WIN":
            s["loss_streak"] = 0

        # 🔒 cooldown після 3 збитків
        if s["loss_streak"] >= 3:
            s["cooldown_until"] = now + 60 * 30  # 30 хв
            s["loss_streak"] = 0

        self._save()

    def blocked(self, pid: str) -> bool:
        if pid not in self.state:
            return False

        return time.time() < self.state[pid]["cooldown_until"]


meta_guard = MetaGuard()
