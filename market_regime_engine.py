class MarketRegimeEngine:

    def detect(self, context_tokens):

        tokens = set(context_tokens)

        if "strong_trend" in tokens:
            return "trend_market"

        if "medium_trend" in tokens:
            return "trend_market"

        if "weak_trend" in tokens:
            return "range_market"

        if "volatility_high" in tokens:
            return "volatile_market"

        if "volatility_low" in tokens:
            return "dead_market"

        return "unknown"