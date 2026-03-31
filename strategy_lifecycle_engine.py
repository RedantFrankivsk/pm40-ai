import json


class StrategyLifecycleEngine:

    def __init__(self):

        self.file = "strategy_lifecycle.json"

        self.testing_threshold = 5
        self.active_threshold = 0.6
        self.weak_threshold = 0.45

        self._ensure_file()

    def _ensure_file(self):

        try:
            with open(self.file, "r"):
                pass
        except:
            with open(self.file, "w") as f:
                json.dump([], f)

    def load(self):

        with open(self.file, "r") as f:
            return json.load(f)

    def save(self, data):

        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

    def register_strategy(self, strategy):

        data = self.load()

        strategy["state"] = "new"
        strategy["trades"] = 0
        strategy["wins"] = 0

        data.append(strategy)

        self.save(data)

    def record_trade(self, pattern, win):

        data = self.load()

        for s in data:

            if s["entry_pattern"] == pattern:

                s["trades"] += 1

                if win:
                    s["wins"] += 1

                winrate = s["wins"] / s["trades"]

                if s["trades"] < self.testing_threshold:
                    s["state"] = "testing"

                elif winrate >= self.active_threshold:
                    s["state"] = "active"

                elif winrate < self.weak_threshold:
                    s["state"] = "retired"

                else:
                    s["state"] = "weak"

        self.save(data)

    def report(self):

        data = self.load()

        return data