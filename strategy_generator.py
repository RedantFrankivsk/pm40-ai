# =========================
# STRATEGY GENERATOR (ULTRA FIX v5)
# =========================

import json
import os


class StrategyGenerator:

    def __init__(self, pattern_file="pattern_memory.json"):
        self.pattern_file = pattern_file
        self.patterns = self.load_patterns()

    # =========================
    def load_patterns(self):
        if not os.path.exists(self.pattern_file):
            return {}

        try:
            with open(self.pattern_file, "r") as f:
                return json.load(f)
        except:
            return {}

    # =========================
    # 🔥 ULTRA NORMALIZER
    # =========================
    def normalize_patterns(self):

        pattern_stats = {}

        # -------- CASE 1: LIST --------
        if isinstance(self.patterns, list):

            for p in self.patterns:
                key = str(p.get("pattern", "unknown"))

                if key not in pattern_stats:
                    pattern_stats[key] = {"trades": 0, "wins": 0}

                pattern_stats[key]["trades"] += 1

                if p.get("result") == "WIN":
                    pattern_stats[key]["wins"] += 1

        # -------- CASE 2: DICT --------
        elif isinstance(self.patterns, dict):

            for key, value in self.patterns.items():

                # 🔥 якщо value = dict (норм)
                if isinstance(value, dict):
                    trades = value.get("trades", 0)
                    wins = value.get("wins", 0)

                # 🔥 якщо value = list (баганий формат)
                elif isinstance(value, list):
                    trades = len(value)
                    wins = sum(1 for x in value if x.get("result") == "WIN")

                else:
                    trades = 0
                    wins = 0

                pattern_stats[key] = {
                    "trades": trades,
                    "wins": wins
                }

        return pattern_stats

    # =========================
    def generate(self):

        pattern_stats = self.normalize_patterns()

        strategies = []

        for pattern, data in pattern_stats.items():

            if not isinstance(data, dict):
                continue

            total = data.get("trades", 0)
            wins = data.get("wins", 0)

            if total == 0:
                continue

            winrate = wins / total

            if total >= 3:

                strategies.append({
                    "pattern": pattern,
                    "trades": total,
                    "wins": wins,
                    "winrate": round(winrate, 2)
                })

        strategies = sorted(strategies, key=lambda x: x["winrate"], reverse=True)

        return strategies

    # =========================
    def build(self):
        return self.generate()

    # =========================
    def print_strategies(self):

        strategies = self.generate()

        print(f"\n[GENERATOR] Built {len(strategies)} strategies\n")

        for s in strategies[:10]:
            print(
                f"{s['pattern']} | trades={s['trades']} | wins={s['wins']} | winrate={s['winrate']}"
            )


# =========================
if __name__ == "__main__":
    sg = StrategyGenerator()
    sg.print_strategies()