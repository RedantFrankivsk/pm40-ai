import json
import os


class BrainEvolutionEngine:

    def __init__(self):

        self.input_file = "selected_strategies.json"
        self.output_file = "evolved_brains.json"

    def load(self):

        if not os.path.exists(self.input_file):
            return []

        with open(self.input_file, "r") as f:
            return json.load(f)

    def load_existing(self):

        if not os.path.exists(self.output_file):
            return []

        with open(self.output_file, "r") as f:
            return json.load(f)

    def save(self, brains):

        with open(self.output_file, "w") as f:
            json.dump(brains, f, indent=4)

    def brain_name(self, pattern):

        name = "_".join(pattern) + "_brain"

        return name

    def evolve(self):

        strategies = self.load()

        existing = self.load_existing()

        existing_names = {b["name"] for b in existing}

        new_brains = []

        for s in strategies:

            pattern = s.get("pattern", [])

            name = self.brain_name(pattern)

            if name in existing_names:
                continue

            brain = {

                "name": name,
                "pattern": pattern,
                "experiment_winrate": s.get("experiment_winrate", 0),
                "forward_winrate": s.get("forward_winrate", 0)
            }

            new_brains.append(brain)

        all_brains = existing + new_brains

        self.save(all_brains)

        return new_brains