import json
import random
import os

from edge_reinforcement_engine import EdgeReinforcementEngine


class ExperimentEngine:

    def __init__(self):

        self.file = "experiments.json"

        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                json.dump([], f)

        self.edge_engine = EdgeReinforcementEngine()

    def load(self):

        with open(self.file, "r") as f:
            return json.load(f)

    def save(self, data):

        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

    def generate_experiments(self):

        experiments = self.load()

        strongest = self.edge_engine.strongest_patterns()

        directions = [
            "follow_trend",
            "reversal",
            "breakout"
        ]

        risks = [
            "fixed",
            "adaptive",
            "dynamic"
        ]

        new_experiments = []

        for p in strongest:

            pattern = p["pattern"]

            exp = {

                "pattern": pattern,

                "direction": random.choice(directions),

                "risk": random.choice(risks),

                "trades": 0,

                "wins": 0,

                "winrate": 0,

                "status": "testing"
            }

            experiments.append(exp)
            new_experiments.append(exp)

        self.save(experiments)

        return new_experiments