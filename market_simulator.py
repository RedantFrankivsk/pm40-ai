import random


class MarketSimulator:

    def __init__(self):
        pass


    def generate_market_for_pattern(self, strategy):

        pattern = strategy["pattern"]

        market = {
            "pattern": pattern,
            "context": random.choice([
                "impulse",
                "correction",
                "consolidation"
            ]),
            "regime": random.choice([
                "trend_market",
                "range_market"
            ])
        }

        return market


    def simulate_trade(self, signal):

        if signal == "NEUTRAL":
            return "neutral"

        r = random.random()

        if r > 0.5:
            return "win"
        else:
            return "loss"