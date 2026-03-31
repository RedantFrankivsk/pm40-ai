import json
import os
import math


class AdaptiveBrainEngine:

    def __init__(self):

        self.experience_file = "experience_memory.json"
        self.config_file = "brain_config.json"

        self.default_config = {
            "signal_threshold": 0.55,
            "strong_threshold": 0.70,
            "neutral_zone": 0.05
        }

    def load_experience(self):

        if not os.path.exists(self.experience_file):
            return []

        with open(self.experience_file, "r") as f:
            return json.load(f)

    def load_config(self):

        if not os.path.exists(self.config_file):
            return self.default_config

        with open(self.config_file, "r") as f:
            return json.load(f)

    def save_config(self, config):

        with open(self.config_file, "w") as f:
            json.dump(config, f, indent=4)

    def analyze_confidence(self, trades):

        high = []
        low = []

        for t in trades:

            confidence = t.get("confidence", 0)

            if confidence >= 0.7:
                high.append(t)

            if confidence <= 0.55:
                low.append(t)

        return high, low

    def winrate(self, trades):

        if not trades:
            return None

        wins = 0

        for t in trades:

            if t.get("result") == "win":
                wins += 1

        return wins / len(trades)

    def adapt(self):

        trades = self.load_experience()

        config = self.load_config()

        if len(trades) < 10:

            return {
                "status": "NOT_ENOUGH_DATA",
                "config": config
            }

        high, low = self.analyze_confidence(trades)

        high_wr = self.winrate(high)
        low_wr = self.winrate(low)

        report = {
            "high_confidence_winrate": high_wr,
            "low_confidence_winrate": low_wr
        }

        if high_wr is not None and high_wr < 0.55:

            config["strong_threshold"] += 0.02

        if low_wr is not None and low_wr > 0.55:

            config["signal_threshold"] -= 0.02

        config["signal_threshold"] = max(0.5, min(0.65, config["signal_threshold"]))
        config["strong_threshold"] = max(0.65, min(0.85, config["strong_threshold"]))

        self.save_config(config)

        report["config"] = config

        return report