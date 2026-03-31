import json
import os
from self_play_training_engine import SelfPlayTrainingEngine
from brain_weighting_engine import BrainWeightingEngine
from adaptive_brain_engine import AdaptiveBrainEngine


class MassiveTrainingLoop:

    def __init__(self):

        self.self_play = SelfPlayTrainingEngine()
        self.weight_engine = BrainWeightingEngine()
        self.adaptive_brain = AdaptiveBrainEngine()

        self.experience_file = "experience_memory.json"

    def load_experience(self):

        if not os.path.exists(self.experience_file):
            return []

        with open(self.experience_file, "r") as f:
            return json.load(f)

    def save_experience(self, trades):

        with open(self.experience_file, "w") as f:
            json.dump(trades, f, indent=4)

    def run(self, cycles=10, trades_per_cycle=100):

        experience = self.load_experience()

        total_wins = 0
        total_trades = 0

        for cycle in range(cycles):

            simulated = self.self_play.run(trades_per_cycle)

            for t in simulated:

                experience.append(t)

                total_trades += 1

                if t["result"] == "win":
                    total_wins += 1

            print("Cycle", cycle + 1, "completed")

        self.save_experience(experience)

        weights = self.weight_engine.update(experience)

        brain_report = self.adaptive_brain.adapt()

        winrate = total_wins / total_trades if total_trades else 0

        return {
            "total_trades": total_trades,
            "wins": total_wins,
            "winrate": round(winrate, 3),
            "brain_weights": weights,
            "brain_report": brain_report
        }