import json
import random


class StrategyGenomeEngine:

    def __init__(self):

        self.population_file = "pattern_population.json"
        self.output_file = "strategy_genomes.json"

        self.directions = [
            "follow_trend",
            "reversal"
        ]

        self.risk_models = [
            "fixed",
            "adaptive"
        ]

    def load_population(self):

        with open(self.population_file, "r") as f:

            return json.load(f)

    def generate_genomes(self):

        population = self.load_population()

        survivors = population["survivors"]

        genomes = []

        for s in survivors:

            pattern = s["pattern"]

            genome = {

                "entry_pattern": pattern,
                "direction": random.choice(self.directions),
                "risk_model": random.choice(self.risk_models),
                "confidence": s["confidence"]
            }

            genomes.append(genome)

        return genomes

    def save(self, genomes):

        with open(self.output_file, "w") as f:

            json.dump(genomes, f, indent=4)

    def run(self):

        genomes = self.generate_genomes()

        self.save(genomes)

        return genomes