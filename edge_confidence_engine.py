import math
from pattern_memory import PatternMemory


class EdgeConfidenceEngine:

    def __init__(self):

        self.memory = PatternMemory()

        self.min_trades = 5

    def score(self, trades, wins):

        if trades == 0:
            return 0

        winrate = wins / trades

        return (winrate - 0.5) * math.log(trades)

    def confidence(self, trades, wins):

        score = self.score(trades, wins)

        return score * math.log(trades + 1)

    def analyze(self):

        patterns = self.memory.all_patterns()

        edges = []

        for pattern in patterns:

            stats = self.memory.get_pattern_stats(pattern)

            trades = stats["trades"]
            wins = stats["wins"]

            if trades < self.min_trades:
                continue

            winrate = wins / trades

            score = self.score(trades, wins)

            conf = self.confidence(trades, wins)

            edges.append({

                "pattern": pattern,
                "trades": trades,
                "winrate": round(winrate, 3),
                "score": round(score, 3),
                "confidence": round(conf, 3)

            })

        edges = sorted(edges, key=lambda x: x["confidence"], reverse=True)

        return edges