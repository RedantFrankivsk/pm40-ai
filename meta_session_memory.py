# meta_session_memory.py
import json
import os

FILE = "meta_session_memory.json"


class MetaSessionMemory:
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

    def register(self, pid: str, session: str, outcome: str):
        self.data.setdefault(pid, {})
        self.data[pid].setdefault(session, {"wins": 0, "losses": 0})

        if outcome == "WIN":
            self.data[pid][session]["wins"] += 1
        elif outcome == "LOSS":
            self.data[pid][session]["losses"] += 1

        self._save()

    def score(self, pid: str, session: str) -> float:
        if pid not in self.data:
            return 0.0
        if session not in self.data[pid]:
            return 0.0

        s = self.data[pid][session]
        total = s["wins"] + s["losses"]
        if total == 0:
            return 0.0

        return (s["wins"] - s["losses"]) / total


meta_session_memory = MetaSessionMemory()
