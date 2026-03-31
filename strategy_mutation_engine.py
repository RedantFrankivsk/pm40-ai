import json
import random


class StrategyMutationEngine:

    def __init__(self):

        self.genome_file = "strategy_genomes.json"
        self.output_file = "mutated_strategies.json"

        self.directions = [
            "follow_trend",
            "reversal"
        ]

        self.risk_models = [
            "fixed",
            "adaptive"
        ]

        self.mutations_per_strategy = 10

    def load_genomes(self):

        with open(self.genome_file, "r") as f:

            return json.load(f)

    def mutate_pattern(self, pattern):

        tokens = pattern.split()

        if len(tokens) <= 1:
            return pattern

        if random.random() < 0.5:

            tokens = tokens[:-1]

        else:

            tokens = tokens[1:]

        return " ".join(tokens)

    def mutate_genome(self, genome):

        new_pattern = self.mutate_pattern(genome["entry_pattern"])

        return {

            "entry_pattern": new_pattern,
            "direction": random.choice(self.directions),
            "risk_model": random.choice(self.risk_models),
            "parent_confidence": genome["confidence"]
        }

    def run(self):

        genomes = self.load_genomes()

        mutated = []

        for g in genomes:

            for _ in range(self.mutations_per_strategy):

                m = self.mutate_genome(g)

                mutated.append(m)

        with open(self.output_file, "w") as f:

            json.dump(mutated, f, indent=4)

        return mutated