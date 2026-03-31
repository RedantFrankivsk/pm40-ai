import json

from strategy_fitness_engine import StrategyFitnessEngine


class StrategySelectionEngine:

    def __init__(self):

        self.output_file = "active_strategies.json"

        self.top_n = 5

        self.fitness_engine = StrategyFitnessEngine()

    def select(self):

        results = self.fitness_engine.evaluate()

        selected = results[:self.top_n]

        with open(self.output_file, "w") as f:

            json.dump(selected, f, indent=4)

        return selected