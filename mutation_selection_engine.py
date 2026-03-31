import json
import os
import random
from walk_forward_engine import WalkForwardEngine


class MutationSelectionEngine:

    def __init__(self):

        self.input_file = "mutation_experiments.json"
        self.output_file = "selected_strategies.json"

        self.walk_forward = WalkForwardEngine()

    def load(self):

        if not os.path.exists(self.input_file):
            return []

        with open(self.input_file, "r") as f:
            return json.load(f)

    def save(self, data):

        with open(self.output_file, "w") as f:
            json.dump(data, f, indent=4)

    def simulate_forward(self, base_winrate):

        noise = random.uniform(-0.05, 0.05)

        forward = base_winrate + noise

        return round(max(0.45, min(0.80, forward)), 3)

    def run(self):

        mutations = self.load()

        selected = []

        for m in mutations:

            # якщо поле відсутнє — додаємо
            if "tested" not in m:
                m["tested"] = False

            if not m["tested"]:
                continue

            winrate = m.get("experiment_winrate", 0)

            if winrate < 0.60:
                continue

            forward = self.simulate_forward(winrate)

            strategy = {

                "pattern": m.get("pattern", []),
                "experiment_winrate": winrate,
                "forward_winrate": forward
            }

            selected.append(strategy)

        self.save(selected)

        return selected