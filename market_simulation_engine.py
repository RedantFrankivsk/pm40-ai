import random


class MarketSimulationEngine:

    def generate_market(self):

        tokens = ["breakout", "pullback", "normal_volume", "low_volume"]
        regimes = ["trend_market", "range_market"]

        return {
            "pattern": random.sample(tokens, 2),
            "context": [],
            "regime": random.choice(regimes)
        }

    def generate_market_for_pattern(self, pattern):

        regime = None
        tokens = []

        for p in pattern:

            if p in ["trend_market", "range_market"]:
                regime = p
            else:
                tokens.append(p)

        if regime is None:
            regime = random.choice(["trend_market", "range_market"])

        return {
            "pattern": tokens,
            "context": [],
            "regime": regime
        }

    def simulate_trade(self, signal):

        if signal == "NEUTRAL":
            return "neutral"

        r = random.random()

        if r > 0.5:
            return "win"
        else:
            return "loss"