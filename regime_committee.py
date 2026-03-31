from brain_committee import BrainCommittee
from regime_detector import RegimeDetector


class RegimeCommittee:

    def __init__(self):

        self.detector = RegimeDetector()

        self.trend_committee = BrainCommittee()
        self.range_committee = BrainCommittee()

    def decide(self, pattern, context, regime):

        regime_type = self.detector.detect(regime)

        if regime_type == "trend":

            decision = self.trend_committee.decide(
                pattern,
                context,
                regime
            )

        elif regime_type == "range":

            decision = self.range_committee.decide(
                pattern,
                context,
                regime
            )

        else:

            decision = {
                "final_signal": "NEUTRAL",
                "confidence": 0
            }

        return decision