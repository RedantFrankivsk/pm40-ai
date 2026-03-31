import json
import os
from brain_committee import BrainCommittee
from market_simulator import MarketSimulator


class StrategyExperimentEngine:

    def __init__(self):

        self.committee = BrainCommittee()
        self.market = MarketSimulator()

        self.file = "strategy_experiments.json"

        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                self.experiments = json.load(f)
        else:
            self.experiments = {}

    def save(self):

        with open(self.file, "w") as f:
            json.dump(self.experiments, f, indent=4)

    def load_discovered_strategies(self):

        with open("discovered_strategies.json", "r") as f:
            return json.load(f)

    def run(self, trades_per_strategy=50):

        strategies = self.load_discovered_strategies()

        for strat in strategies:

            key = str(strat)

            if key not in self.experiments:

                self.experiments[key] = {
                    "pattern": strat,
                    "trades": 0,
                    "wins": 0,
                    "status": "testing"
                }

            if self.experiments[key]["status"] != "testing":
                continue

            for _ in range(trades_per_strategy):

                market = self.market.generate_market_for_pattern(strat)

                decision = self.committee.decide(
                    market["pattern"],
                    market["context"],
                    market["regime"]
                )

                signal = decision["final_signal"]

                result = self.market.simulate_trade(signal)

                if result == "neutral":
                    continue

                self.experiments[key]["trades"] += 1

                if result == "win":
                    self.experiments[key]["wins"] += 1

            trades = self.experiments[key]["trades"]
            wins = self.experiments[key]["wins"]

            if trades >= 100:

                winrate = wins / trades

                if winrate >= 0.6:
                    self.experiments[key]["status"] = "promoted"
                else:
                    self.experiments[key]["status"] = "rejected"

        self.save()

        return self.experiments