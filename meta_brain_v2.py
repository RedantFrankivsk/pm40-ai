import json
import os
from brain_memory import BrainMemory


class MetaBrain:

    def __init__(self):

        self.brain_file = "ranked_brains.json"

        self.memory = BrainMemory()

        if os.path.exists(self.brain_file):
            with open(self.brain_file, "r") as f:
                self.brains = json.load(f)
        else:
            self.brains = []

    def detect_regime(self, description):

        description = description.lower()

        if "trend" in description:
            return "trend_market"

        if "range" in description:
            return "range_market"

        return "unknown"

    def compute_live_score(self, brain):

        stats = self.memory.get_brain_stats(brain["name"])

        return stats["winrate"]

    def compute_final_score(self, brain):

        forward = brain.get("forward_winrate", 0)
        experiment = brain.get("experiment_winrate", 0)

        live = self.compute_live_score(brain)

        score = (
            forward * 0.5
            + experiment * 0.25
            + live * 0.25
        )

        return round(score, 3)

    def choose_brain(self, description):

        regime = self.detect_regime(description)

        candidates = []

        for brain in self.brains:

            pattern = brain.get("pattern", [])

            if regime in pattern:
                candidates.append(brain)

        if not candidates:
            candidates = self.brains

        best = None
        best_score = 0

        for brain in candidates:

            score = self.compute_final_score(brain)

            if score > best_score:

                best_score = score
                best = brain

        return best, best_score, regime

    def get_signal(self, description):

        brain, score, regime = self.choose_brain(description)

        if brain is None:

            return {
                "signal": "NEUTRAL"
            }

        pattern = brain.get("pattern", [])

        if "breakout" in pattern:
            signal = "UP"

        elif "pullback" in pattern:
            signal = "DOWN"

        else:
            signal = "NEUTRAL"

        self.memory.record_signal(
            brain["name"],
            pattern,
            signal
        )

        return {

            "brain": brain["name"],
            "pattern": pattern,
            "signal": signal,
            "score": score,
            "regime": regime
        }