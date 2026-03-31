import json
import os


class PatternIntelligenceEngine:

    def __init__(self):

        self.file = "experience_memory.json"

    def load_trades(self):

        if not os.path.exists(self.file):
            return []

        with open(self.file, "r") as f:
            return json.load(f)

    def analyze(self):

        trades = self.load_trades()

        stats = {}

        for t in trades:

            pattern = tuple(sorted(t["pattern"]))

            if pattern not in stats:
                stats[pattern] = {
                    "trades": 0,
                    "wins": 0
                }

            stats[pattern]["trades"] += 1

            if t["result"] == "win":
                stats[pattern]["wins"] += 1

        results = []

        for p in stats:

            trades = stats[p]["trades"]
            wins = stats[p]["wins"]

            if trades < 5:
                continue

            winrate = wins / trades

            results.append({
                "pattern": p,
                "trades": trades,
                "wins": wins,
                "winrate": round(winrate, 3)
            })

        results.sort(key=lambda x: x["winrate"], reverse=True)

        return results