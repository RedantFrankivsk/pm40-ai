from base_brain import BaseBrain


class TrendBrain(BaseBrain):

    def __init__(self):

        super().__init__("TrendBrain")

    def evaluate(self, pattern_tokens, context_tokens, regime):

        score = 0.5

        if "trend_market" in pattern_tokens:
            score += 0.1

        if "strong_trend" in context_tokens:
            score += 0.1

        if "pullback" in pattern_tokens:
            score += 0.05

        if score > 0.6:
            signal = "UP"
        elif score < 0.45:
            signal = "DOWN"
        else:
            signal = "NEUTRAL"

        return {
            "brain": self.name,
            "signal": signal,
            "confidence": round(score, 3)
        }