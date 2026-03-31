import json
import os


class BrainWeightingEngine:

    def __init__(self):

        self.file = "brain_weights.json"

        self.default = {
            "TrendBrain": 1.0,
            "ReversalBrain": 1.0
        }

    def load(self):

        if not os.path.exists(self.file):
            return self.default.copy()

        with open(self.file, "r") as f:
            return json.load(f)

    def save(self, weights):

        with open(self.file, "w") as f:
            json.dump(weights, f, indent=4)

    def update(self, trades):

        weights = self.load()

        stats = {}

        for t in trades:

            brain = t.get("brain")

            if brain is None:
                continue

            if brain == "null":
                continue

            if brain not in stats:
                stats[brain] = {"trades": 0, "wins": 0}

            stats[brain]["trades"] += 1

            if t.get("result") == "win":
                stats[brain]["wins"] += 1

        for brain in stats:

            trades_count = stats[brain]["trades"]
            wins = stats[brain]["wins"]

            if trades_count < 5:
                continue

            winrate = wins / trades_count

            if winrate > 0.6:
                weights[brain] = min(weights.get(brain, 1.0) + 0.1, 2.0)

            elif winrate < 0.45:
                weights[brain] = max(weights.get(brain, 1.0) - 0.1, 0.5)

        self.save(weights)

        return weights