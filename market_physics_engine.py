import random


class MarketPhysicsEngine:

    def __init__(self):

        pass

    def trend_continuation(self, signal):

        if signal == "UP":
            return random.choices(["win", "loss"], weights=[0.65, 0.35])[0]

        if signal == "DOWN":
            return random.choices(["win", "loss"], weights=[0.35, 0.65])[0]

        return "loss"

    def range_behavior(self, signal):

        if signal == "DOWN":
            return random.choices(["win", "loss"], weights=[0.6, 0.4])[0]

        if signal == "UP":
            return random.choices(["win", "loss"], weights=[0.4, 0.6])[0]

        return random.choice(["win", "loss"])

    def volatility_shock(self):

        return random.random() < 0.1

    def evaluate_trade(self, signal, regime):

        if self.volatility_shock():
            return random.choice(["win", "loss"])

        if regime == "trend_market":
            return self.trend_continuation(signal)

        if regime == "range_market":
            return self.range_behavior(signal)

        return random.choice(["win", "loss"])