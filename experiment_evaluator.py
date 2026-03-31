import json
import os


class ExperimentEvaluator:

    def __init__(self):

        self.exp_file = "experiments.json"
        self.strat_file = "active_strategies.json"

    def load_experiments(self):

        if not os.path.exists(self.exp_file):
            return []

        with open(self.exp_file, "r") as f:
            return json.load(f)

    def load_strategies(self):

        if not os.path.exists(self.strat_file):
            return []

        with open(self.strat_file, "r") as f:
            return json.load(f)

    def save_experiments(self, data):

        with open(self.exp_file, "w") as f:
            json.dump(data, f, indent=4)

    def save_strategies(self, data):

        with open(self.strat_file, "w") as f:
            json.dump(data, f, indent=4)

    def evaluate(self):

        experiments = self.load_experiments()
        strategies = self.load_strategies()

        promoted = []
        failed = []

        for e in experiments:

            if e["status"] != "testing":
                continue

            if e["trades"] < 5:
                continue

            winrate = e["wins"] / e["trades"]

            if winrate >= 0.6:

                strat = {

                    "pattern": e["pattern"],
                    "direction": e["direction"],
                    "risk": e["risk"],
                    "confidence": winrate
                }

                strategies.append(strat)

                e["status"] = "promoted"

                promoted.append(strat)

            elif winrate < 0.4:

                e["status"] = "failed"

                failed.append(e)

        self.save_experiments(experiments)
        self.save_strategies(strategies)

        return promoted, failed