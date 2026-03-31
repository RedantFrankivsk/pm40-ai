# meta_memory.py
import json
import time
import os

FILE = "meta_memory.json"


class MetaMemory:
    def __init__(self):
        self.data = {}
        self._load()

    def _load(self):
        if os.path.exists(FILE):
            with open(FILE, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        else:
            self.data = {}

    def _save(self):
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2)

    def register(self, pid: str, outcome: str):
        now = time.time()

        if pid not in self.data:
            self.data[pid] = {
                "wins": 0,
                "losses": 0,
                "last_seen": now
            }

        if outcome == "WIN":
            self.data[pid]["wins"] += 1
        elif outcome == "LOSS":
            self.data[pid]["losses"] += 1

        self.data[pid]["last_seen"] = now
        self._save()

    def score(self, pid: str) -> float:
        if pid not in self.data:
            return 0.0

        p = self.data[pid]
        total = p["wins"] + p["losses"]
        if total == 0:
            return 0.0

        # forgetting
        age_hours = (time.time() - p["last_seen"]) / 3600
        decay = max(0.3, 1 - age_hours / 72)

        raw = (p["wins"] - p["losses"]) / total
        return round(raw * decay, 2)


meta_memory = MetaMemory()
