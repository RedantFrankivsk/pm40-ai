import random


class BaseBrain:

    def __init__(self, name):

        self.name = name

    def evaluate(self, pattern_tokens, context_tokens, regime):

        score = random.uniform(0.45, 0.65)

        if score > 0.55:
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