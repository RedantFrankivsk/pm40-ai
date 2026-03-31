# anti_overfitting_engine.py

import json
import os


class AntiOverfittingEngine:

    def __init__(self):
        self.input_file = "strategy_discovery.json"
        self.output_file = "strategy_filtered.json"

    def load(self):
        if not os.path.exists(self.input_file):
            return []

        try:
            with open(self.input_file, "r") as f:
                return json.load(f)
        except:
            return []

    def save(self, strategies):
        with open(self.output_file, "w") as f:
            json.dump(strategies, f, indent=4)

    def adjust_winrate(self, winrate, trades):
        """
        Penalize low sample size (anti-overfitting)
        """

        if trades < 3:
            penalty = 0.03
        elif trades < 5:
            penalty = 0.02
        elif trades < 10:
            penalty = 0.01
        else:
            penalty = 0.0

        return round(winrate - penalty, 3)

    def run(self):
        strategies = self.load()
        filtered = []

        for s in strategies:
            trades = s.get("trades", 0)
            winrate = s.get("winrate", 0)

            adjusted = self.adjust_winrate(winrate, trades)

            status = "candidate"

            if trades < 3:
                status = "weak_candidate"

            s["adjusted_winrate"] = adjusted
            s["status"] = status

            # 🔥 головний фільтр
            if adjusted >= 0.50:
                filtered.append(s)

        self.save(filtered)

        return filtered