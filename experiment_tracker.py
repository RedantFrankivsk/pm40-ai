import json
import os


class ExperimentTracker:

    def __init__(self):

        self.file = "experiments.json"

    def load(self):

        if not os.path.exists(self.file):
            return []

        with open(self.file, "r") as f:
            return json.load(f)

    def save(self, data):

        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

    def update(self, trade):

        """
        trade structure:

        {
            pattern
            direction
            result
        }
        """

        experiments = self.load()

        for e in experiments:

            if e["status"] != "testing":
                continue

            if e["pattern"] != trade["pattern"]:
                continue

            if e["direction"] != trade["direction"]:
                continue

            e["trades"] += 1

            if trade["result"] == "win":
                e["wins"] += 1

            if e["trades"] > 0:
                e["winrate"] = e["wins"] / e["trades"]

        self.save(experiments)