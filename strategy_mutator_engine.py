import json
import os
import random


class StrategyMutatorEngine:

    def __init__(self):

        self.input_file = "strategy_filtered.json"
        self.output_file = "strategy_mutations.json"

        self.mutation_pool = [
            "high_volume",
            "low_volume",
            "volatility_high",
            "volatility_low",
            "session_london",
            "session_newyork",
            "strong_trend"
        ]

    def load_strategies(self):

        if not os.path.exists(self.input_file):
            return []

        with open(self.input_file, "r") as f:
            return json.load(f)

    def save(self, mutations):

        with open(self.output_file, "w") as f:
            json.dump(mutations, f, indent=4)

    def normalize_pattern(self, pattern):

        return sorted(list(set(pattern)))

    def mutate_pattern(self, pattern):

        mutation = random.choice(self.mutation_pool)

        new_pattern = pattern + [mutation]

        return self.normalize_pattern(new_pattern)

    def run(self):

        strategies = self.load_strategies()

        mutations = []

        for s in strategies:

            base_pattern = s["pattern"]

            for _ in range(3):

                new_pattern = self.mutate_pattern(base_pattern)

                mutation = {

                    "pattern": new_pattern,
                    "base_pattern": base_pattern,
                    "source_winrate": s.get("adjusted_winrate", s.get("winrate", 0))
                }

                mutations.append(mutation)

        self.save(mutations)

        return mutations