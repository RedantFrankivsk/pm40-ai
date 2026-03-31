import json
import os
import random


class GeneticEvolutionEngine:

    def __init__(self):

        self.brain_file = "evolved_brains.json"

        if not os.path.exists(self.brain_file):
            self.brains = []
        else:
            with open(self.brain_file, "r") as f:
                self.brains = json.load(f)

    def save(self):

        with open(self.brain_file, "w") as f:
            json.dump(self.brains, f, indent=4)

    def normalize_pattern(self, pattern):

        return sorted(list(set(pattern)))

    def combine_patterns(self, p1, p2):

        combined = p1 + p2

        return self.normalize_pattern(combined)

    def create_brain_name(self, pattern):

        return "_".join(pattern) + "_brain"

    def evolve(self):

        if len(self.brains) < 2:
            return []

        new_brains = []

        existing_names = set(b["name"] for b in self.brains)

        for _ in range(10):

            b1 = random.choice(self.brains)
            b2 = random.choice(self.brains)

            pattern = self.combine_patterns(b1["pattern"], b2["pattern"])

            name = self.create_brain_name(pattern)

            if name in existing_names:
                continue

            new_brain = {

                "name": name,
                "pattern": pattern,
                "experiment_winrate": round(
                    (b1["experiment_winrate"] + b2["experiment_winrate"]) / 2, 3
                ),
                "forward_winrate": round(
                    (b1["forward_winrate"] + b2["forward_winrate"]) / 2, 3
                ),
                "genetic": True
            }

            self.brains.append(new_brain)
            new_brains.append(new_brain)

            existing_names.add(name)

        self.save()

        return new_brains