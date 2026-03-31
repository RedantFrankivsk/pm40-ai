import math
import itertools

try:
    from pattern_memory_MARCH import PatternMemory
except Exception:
    try:
        from pattern_memory import PatternMemory
    except Exception:
        PatternMemory = None


class StructuralEdgeEngine:

    def __init__(self):

        if PatternMemory:
            self.memory = PatternMemory()
        else:
            self.memory = None

        # 🔥 ЗНИЖЕНО ДЛЯ СТАРТУ
        self.min_trades = 3
        self.min_score = 0.01

        # 🔥 TTL кеш (оновлюється)
        self._cache = None
        self._last_update = 0
        self.cache_ttl = 30  # секунд

    def score(self, trades, wins):

        if trades == 0:
            return 0

        winrate = wins / trades

        return (winrate - 0.5) * math.log(trades + 1)

    def generate_structures(self, tokens):

        structures = []

        for r in range(2, min(len(tokens), 4) + 1):
            combos = itertools.combinations(tokens, r)

            for c in combos:
                structures.append(" ".join(sorted(c)))

        return structures

    def _get_patterns(self):

        if not self.memory:
            return []

        if hasattr(self.memory, "all_patterns"):
            return self.memory.all_patterns()

        if hasattr(self.memory, "get_all_patterns"):
            return self.memory.get_all_patterns()

        if hasattr(self.memory, "data"):
            return list(self.memory.data.keys())

        print("[EDGE] ⚠️ unknown memory structure")
        return []

    def _get_stats(self, pattern):

        if not self.memory:
            return {"trades": 0, "wins": 0, "winrate": 0}

        stats = None

        if hasattr(self.memory, "get_pattern_stats"):
            stats = self.memory.get_pattern_stats(pattern)

        elif hasattr(self.memory, "get_stats"):
            stats = self.memory.get_stats(pattern)

        elif hasattr(self.memory, "data"):
            stats = self.memory.data.get(pattern, {"trades": 0, "wins": 0})

        if not stats:
            return {"trades": 0, "wins": 0, "winrate": 0}

        trades = stats.get("trades", 0)
        wins = stats.get("wins", 0)

        if "winrate" in stats and trades > 0:
            winrate = stats["winrate"]
            wins = int(winrate * trades)

        return {
            "trades": trades,
            "wins": wins,
            "winrate": stats.get("winrate", 0)
        }

    def discover(self):

        import time

        now = time.time()

        # 🔥 КЕШ З TTL
        if self._cache is not None and (now - self._last_update) < self.cache_ttl:
            return self._cache

        patterns = self._get_patterns()

        if not patterns:
            print("[EDGE] no patterns in memory")
            self._cache = []
            self._last_update = now
            return []

        structure_stats = {}

        total_patterns = 0

        for pattern in patterns:

            tokens = pattern.split()

            stats = self._get_stats(pattern)

            trades = stats.get("trades", 0)
            wins = stats.get("wins", 0)

            if trades == 0:
                continue

            total_patterns += 1

            structures = self.generate_structures(tokens)

            for s in structures:

                if s not in structure_stats:
                    structure_stats[s] = {
                        "trades": 0,
                        "wins": 0
                    }

                structure_stats[s]["trades"] += trades
                structure_stats[s]["wins"] += wins

        if total_patterns == 0:
            print("[EDGE] no usable stats yet")
            self._cache = []
            self._last_update = now
            return []

        edges = []

        for s in structure_stats:

            trades = structure_stats[s]["trades"]
            wins = structure_stats[s]["wins"]

            if trades < self.min_trades:
                continue

            score = self.score(trades, wins)

            if score < self.min_score:
                continue

            winrate = wins / trades if trades > 0 else 0

            edges.append({
                "structure": s,
                "trades": trades,
                "winrate": round(winrate, 3),
                "score": round(score, 3)
            })

        edges = sorted(edges, key=lambda x: x["score"], reverse=True)

        # 🔥 DEBUG
        print(f"[EDGE DEBUG] patterns={len(patterns)} usable={total_patterns} edges={len(edges)}")

        if edges:
            top = edges[0]
            print(f"[EDGE] top: {top['structure']} | wr={top['winrate']} | trades={top['trades']}")

        self._cache = edges
        self._last_update = now

        return edges