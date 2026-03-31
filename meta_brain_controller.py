import json
import os


class MetaBrainController:

    def __init__(self):

        self.brain_file = "evolved_brains.json"

        if not os.path.exists(self.brain_file):
            self.brains = []
        else:
            with open(self.brain_file, "r") as f:
                self.brains = json.load(f)

    def detect_regime(self, description):

        description = description.lower()

        if "range" in description or "flat" in description:
            return "range_market"

        return "trend_market"

    def filter_brains_by_regime(self, regime):

        filtered = []

        for brain in self.brains:

            pattern = brain["pattern"]

            if regime in pattern:
                filtered.append(brain)

        return filtered

    def choose_best_brain(self, brains):

        if not brains:
            return None

        best = None
        best_score = 0

        for b in brains:

            score = b["forward_winrate"]

            if score > best_score:
                best_score = score
                best = b

        return best

    def analyze(self, description):

        regime = self.detect_regime(description)

        regime_brains = self.filter_brains_by_regime(regime)

        best_brain = self.choose_best_brain(regime_brains)

        if best_brain is None:

            return {
                "signal": "NEUTRAL",
                "reason": "no suitable brain",
                "regime": regime
            }

        pattern = best_brain["pattern"]

        if "breakout" in pattern and "trend_market" in pattern:
            signal = "UP"

        elif "range_market" in pattern:
            signal = "NEUTRAL"

        else:
            signal = "DOWN"

        return {

            "signal": signal,
            "brain": best_brain["name"],
            "forward_winrate": best_brain["forward_winrate"],
            "regime": regime
        }