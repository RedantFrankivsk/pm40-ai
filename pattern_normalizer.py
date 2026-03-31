class PatternNormalizer:

    def __init__(self):

        self.remove_tokens = {

            "session_london",
            "session_ny",
            "session_asia",

            "volatility_low",
            "volatility_normal",
            "volatility_high",

            "strong_trend",
            "medium_trend",
            "weak_trend",

            "5m_uptrend",
            "10m_uptrend",
            "15m_uptrend",
            "5m_downtrend",
            "10m_downtrend",
            "15m_downtrend"
        }

    def normalize(self, pattern):

        tokens = pattern.split()

        tokens = [t for t in tokens if t not in self.remove_tokens]

        tokens = sorted(set(tokens))

        return " ".join(tokens)