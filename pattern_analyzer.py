import json
import os


class PatternAnalyzer:

    def __init__(self):

        self.file = "pattern_memory.json"

        if not os.path.exists(self.file):
            self.memory = {}
        else:
            with open(self.file, "r") as f:
                self.memory = json.load(f)

    def get_statistics(self):

        stats = []

        for pattern, data in self.memory.items():

            wins = data["wins"]
            losses = data["losses"]

            total = wins + losses

            if total == 0:
                continue

            winrate = wins / total

            stats.append({
                "pattern": pattern,
                "wins": wins,
                "losses": losses,
                "total": total,
                "winrate": winrate
            })

        return stats


    def strongest_patterns(self, min_trades=10):

        strong = []

        for s in self.get_statistics():

            if s["total"] >= min_trades and s["winrate"] > 0.6:
                strong.append(s)

        strong.sort(key=lambda x: x["winrate"], reverse=True)

        return strong


    def weakest_patterns(self, min_trades=10):

        weak = []

        for s in self.get_statistics():

            if s["total"] >= min_trades and s["winrate"] < 0.4:
                weak.append(s)

        weak.sort(key=lambda x: x["winrate"])

        return weak