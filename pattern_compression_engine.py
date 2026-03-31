# pattern_compression_engine.py

from itertools import combinations
from pattern_memory import PatternMemory
import math


class PatternCompressionEngine:

    def __init__(self):

        self.memory = PatternMemory()


    def compress(self, pattern):

        tokens = pattern.split()

        compressed_patterns = []

        for r in range(2, len(tokens) + 1):

            combos = combinations(tokens, r)

            for combo in combos:

                compressed_patterns.append(" ".join(sorted(combo)))

        return list(set(compressed_patterns))


    def evaluate(self, pattern):

        compressed = self.compress(pattern)

        results = []

        for p in compressed:

            stats = self.memory.get_pattern_stats(p)

            trades = stats["trades"]
            wins = stats["wins"]

            if trades < 20:
                continue

            winrate = wins / trades

            score = (winrate - 0.5) * math.log(trades)

            results.append({
                "pattern": p,
                "trades": trades,
                "winrate": winrate,
                "score": score
            })

        results.sort(key=lambda x: x["score"], reverse=True)

        return results