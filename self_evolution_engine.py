import json
import random
from edge_reinforcement_engine import EdgeReinforcementEngine


class SelfEvolutionEngine:

    def __init__(self):

        self.strategy_file = "active_strategies.json"
        self.edge_engine = EdgeReinforcementEngine()

    def load_strategies(self):

        try:
            with open(self.strategy_file, "r") as f:
                return json.load(f)
        except:
            return []

    def save_strategies(self, strategies):

        with open(self.strategy_file, "w") as f:
            json.dump(strategies, f, indent=4)

    def generate_strategy(self, pattern):

        directions = ["follow_trend", "reversal"]
        risks = ["fixed", "adaptive"]

        strategy = {
            "pattern": pattern,
            "direction": random.choice(directions),
            "risk": random.choice(risks),
            "confidence": 0.0
        }

        return strategy

    def evolve(self):

        strongest = self.edge_engine.strongest_patterns()

        current = self.load_strategies()

        new_strategies = []

        for p in strongest:

            pattern = p["pattern"]

            strategy = self.generate_strategy(pattern)

            new_strategies.append(strategy)

        combined = current + new_strategies

        unique = []
        seen = set()

        for s in combined:

            pattern = s.get("pattern") or s.get("entry_pattern")
            direction = s.get("direction")
            risk = s.get("risk")

            if pattern is None or direction is None or risk is None:
                continue

            key = (pattern, direction, risk)

            if key not in seen:

                seen.add(key)

                unique.append({
                    "pattern": pattern,
                    "direction": direction,
                    "risk": risk,
                    "confidence": s.get("confidence", 0.0)
                })

        self.save_strategies(unique)

        return new_strategies