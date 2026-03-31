import json
import os


class BrainRankingEngine:

    def __init__(self):

        self.input_file = "evolved_brains.json"
        self.output_file = "ranked_brains.json"

    def load(self):

        if not os.path.exists(self.input_file):
            return []

        with open(self.input_file, "r") as f:
            return json.load(f)

    def save(self, brains):

        with open(self.output_file, "w") as f:
            json.dump(brains, f, indent=4)

    def compute_score(self, brain):

        forward = brain.get("forward_winrate", 0)
        experiment = brain.get("experiment_winrate", 0)

        pattern = brain.get("pattern", [])

        pattern_bonus = len(pattern) * 0.01

        score = (
            forward * 0.6
            + experiment * 0.3
            + pattern_bonus
        )

        return round(score, 3)

    def run(self):

        brains = self.load()

        ranked = []

        for b in brains:

            score = self.compute_score(b)

            b["score"] = score

            ranked.append(b)

        ranked = sorted(ranked, key=lambda x: x["score"], reverse=True)

        self.save(ranked)

        return ranked