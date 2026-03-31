from regime_strategy_engine import RegimeStrategyEngine
from market_regime_engine import MarketRegimeEngine


class PM40Brain:

    def __init__(self):

        self.strategy_engine = RegimeStrategyEngine()
        self.regime_engine = MarketRegimeEngine()

    def analyze(self, pattern_tokens, context_tokens):

        regime = self.regime_engine.detect(context_tokens)

        strategies = self.strategy_engine.match_strategy(
            pattern_tokens,
            context_tokens
        )

        if not strategies:

            return {
                "signal": "NEUTRAL",
                "regime": regime,
                "strategy": None
            }

        best = strategies[0]

        direction = best["direction"]

        if direction == "follow_trend":

            signal = "UP"

        elif direction == "reversal":

            signal = "DOWN"

        else:

            signal = "NEUTRAL"

        return {
            "signal": signal,
            "regime": regime,
            "strategy": best
        }