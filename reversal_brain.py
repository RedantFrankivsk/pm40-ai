from base_brain import BaseBrain


class ReversalBrain(BaseBrain):

    def __init__(self):

        super().__init__("ReversalBrain")

    def evaluate(self, pattern_tokens, context_tokens, regime):

        score = 0.5

        if "range_market" in pattern_tokens:
            score += 0.1

        if "weak_trend" in context_tokens:
            score += 0.1

        if "pullback" in pattern_tokens:
            score -= 0.05

        if score > 0.6:
            signal = "DOWN"
        elif score < 0.45:
            signal = "UP"
        else:
            signal = "NEUTRAL"

        return {
            "brain": self.name,
            "signal": signal,
            "confidence": round(score, 3)
        }