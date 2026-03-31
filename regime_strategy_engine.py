import json

from market_regime_engine import MarketRegimeEngine


class RegimeStrategyEngine:

    def __init__(self):

        self.strategy_file = "active_strategies.json"

        self.regime_engine = MarketRegimeEngine()

    def load_strategies(self):

        with open(self.strategy_file, "r") as f:

            return json.load(f)

    def match_strategy(self, pattern_tokens, context_tokens):

        strategies = self.load_strategies()

        regime = self.regime_engine.detect(context_tokens)

        pattern_set = set(pattern_tokens)

        matches = []

        for s in strategies:

            strategy_pattern = set(s["entry_pattern"].split())

            if strategy_pattern.issubset(pattern_set):

                matches.append({
                    "pattern": s["entry_pattern"],
                    "direction": s["direction"],
                    "risk": s["risk_model"],
                    "regime": regime
                })

        return matches