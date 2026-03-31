import math
from pattern_memory import PatternMemory


class MarketDNAEngine:

    def __init__(self):

        self.memory = PatternMemory()

        self.min_trades = 10

    def score(self, trades, wins):

        if trades == 0:
            return 0

        winrate = wins / trades

        return (winrate - 0.5) * math.log(trades)

    def build_map(self):

        patterns = self.memory.all_patterns()

        dna = []

        for pattern in patterns:

            stats = self.memory.get_pattern_stats(pattern)

            trades = stats["trades"]
            wins = stats["wins"]

            if trades < self.min_trades:
                continue

            winrate = wins / trades

            score = self.score(trades, wins)

            dna.append({

                "pattern": pattern,
                "trades": trades,
                "winrate": round(winrate, 3),
                "score": round(score, 3)

            })

        dna = sorted(dna, key=lambda x: x["score"], reverse=True)

        return dna