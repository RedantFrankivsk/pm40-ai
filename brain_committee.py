from trend_brain import TrendBrain
from reversal_brain import ReversalBrain
from brain_weighting_engine import BrainWeightingEngine


class BrainCommittee:

    def __init__(self):

        self.brains = [
            TrendBrain(),
            ReversalBrain()
        ]

        self.weight_engine = BrainWeightingEngine()

    def decide(self, pattern_tokens, context_tokens, regime):

        weights = self.weight_engine.load()

        votes = []

        score_up = 0
        score_down = 0

        for brain in self.brains:

            result = brain.evaluate(
                pattern_tokens,
                context_tokens,
                regime
            )

            result["brain"] = brain.name

            weight = weights.get(brain.name, 1.0)

            result["weight"] = weight

            votes.append(result)

            if result["signal"] == "UP":
                score_up += weight

            if result["signal"] == "DOWN":
                score_down += weight

        if score_up > score_down:
            final = "UP"
        elif score_down > score_up:
            final = "DOWN"
        else:
            final = "NEUTRAL"

        return {
            "final_signal": final,
            "votes": votes
        }