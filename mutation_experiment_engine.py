import json
import os
import random


class MutationExperimentEngine:

    def __init__(self):

        self.input_file = "strategy_mutations.json"
        self.output_file = "mutation_experiments.json"

    def load(self):

        if not os.path.exists(self.input_file):
            return []

        with open(self.input_file, "r") as f:
            return json.load(f)

    def save(self, data):

        with open(self.output_file, "w") as f:
            json.dump(data, f, indent=4)

    def simulate_winrate(self, pattern):

        base = 0.55

        bonus = 0.0

        if "trend_market" in pattern:
            bonus += 0.03

        if "pullback" in pattern:
            bonus += 0.02

        if "breakout" in pattern:
            bonus += 0.02

        if "volatility_high" in pattern:
            bonus += 0.01

        if "strong_trend" in pattern:
            bonus += 0.02

        noise = random.uniform(-0.03, 0.03)

        winrate = base + bonus + noise

        return round(max(0.45, min(0.75, winrate)), 3)

    def run(self):

        mutations = self.load()

        results = []

        for m in mutations:

            # якщо поля немає — створюємо
            if "tested" not in m:
                m["tested"] = False

            if m["tested"]:
                results.append(m)
                continue

            pattern = m.get("pattern", [])

            winrate = self.simulate_winrate(pattern)

            m["experiment_winrate"] = winrate
            m["tested"] = True

            results.append(m)

        self.save(results)

        return results