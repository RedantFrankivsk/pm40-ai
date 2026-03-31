# pattern_evolution_engine.py

from pattern_mutation_engine import PatternMutationEngine
from pattern_memory import PatternMemory
import math


class PatternEvolutionEngine:

    def __init__(self):

        self.memory = PatternMemory()
        self.mutator = PatternMutationEngine()


    def evolve(self, base_pattern):

        mutations = self.mutator.mutate(base_pattern, 10)

        # remove duplicate mutations
        unique_patterns = list(set(mutations))

        results = []

        for pattern in unique_patterns:

            stats = self.memory.get_pattern_stats(pattern)

            trades = stats["trades"]
            wins = stats["wins"]

            if trades == 0:
                continue

            winrate = wins / trades

            score = (winrate - 0.5) * math.log(trades)

            results.append({
                "pattern": pattern,
                "trades": trades,
                "winrate": winrate,
                "score": score
            })

        results.sort(key=lambda x: x["score"], reverse=True)

        return results