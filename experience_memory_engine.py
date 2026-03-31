import json
import time


class ExperienceMemoryEngine:

    def __init__(self):

        self.file = "experience_memory.json"

        self._ensure_file()

    def _ensure_file(self):

        try:
            with open(self.file, "r"):
                pass
        except:
            with open(self.file, "w") as f:
                json.dump([], f)

    def load(self):

        with open(self.file, "r") as f:
            return json.load(f)

    def save(self, data):

        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

    def record_experience(
        self,
        signal,
        pattern_tokens,
        context_tokens,
        regime,
        strategy,
        confidence,
        result
    ):

        data = self.load()

        entry = {
            "timestamp": int(time.time()),
            "signal": signal,
            "pattern": " ".join(pattern_tokens),
            "context": context_tokens,
            "regime": regime,
            "strategy_pattern": strategy["pattern"] if strategy else None,
            "direction": strategy["direction"] if strategy else None,
            "risk": strategy["risk"] if strategy else None,
            "confidence": confidence,
            "result": result
        }

        data.append(entry)

        self.save(data)

    def all_experiences(self):

        return self.load()

    def stats(self):

        data = self.load()

        total = len(data)

        wins = 0
        losses = 0

        for e in data:

            if e["result"] == "WIN":
                wins += 1

            if e["result"] == "LOSS":
                losses += 1

        winrate = wins / total if total > 0 else 0

        return {
            "total": total,
            "wins": wins,
            "losses": losses,
            "winrate": winrate
        }