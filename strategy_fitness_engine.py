import json
import math

from pattern_memory import PatternMemory
from edge_confidence_engine import EdgeConfidenceEngine


class StrategyFitnessEngine:

    def __init__(self):

        self.strategy_file = "mutated_strategies.json"

        self.memory = PatternMemory()
        self.conf_engine = EdgeConfidenceEngine()

    def load_strategies(self):

        with open(self.strategy_file, "r") as f:

            return json.load(f)

    def compute_fitness(self, pattern):

        stats = self.memory.get_pattern_stats(pattern)

        trades = stats["trades"]

        if trades == 0:
            return 0, 0, 0

        wins = stats["wins"]

        winrate = wins / trades

        score = (winrate - 0.5) * math.log(trades)

        confidence = score * math.log(trades)

        fitness = confidence * math.log(trades + 1)

        return trades, winrate, fitness

    def evaluate(self):

        strategies = self.load_strategies()

        results = []

        for s in strategies:

            pattern = s["entry_pattern"]

            trades, winrate, fitness = self.compute_fitness(pattern)

            s["trades"] = trades
            s["winrate"] = winrate
            s["fitness"] = fitness

            results.append(s)

        results.sort(key=lambda x: x["fitness"], reverse=True)

        return results