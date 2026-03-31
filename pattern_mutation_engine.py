# pattern_mutation_engine.py

import random


class PatternMutationEngine:

    def __init__(self):

        self.volume_states = [
            "low_volume",
            "normal_volume",
            "high_volume"
        ]

        self.market_regimes = [
            "trend_market",
            "range_market"
        ]

        self.sessions = [
            "session_london",
            "session_ny",
            "session_asia"
        ]

        self.volatility_states = [
            "volatility_low",
            "volatility_normal",
            "volatility_high"
        ]

        self.trend_strength_states = [
            "weak_trend",
            "medium_trend",
            "strong_trend"
        ]


    def mutate(self, pattern, count=10):

        tokens = pattern.split()

        mutations = []

        for _ in range(count):

            new_tokens = tokens.copy()

            mutation_type = random.choice([
                "volume",
                "regime",
                "session",
                "volatility",
                "trend_strength"
            ])

            if mutation_type == "volume":

                new_tokens = [t for t in new_tokens if "volume" not in t]
                new_tokens.append(random.choice(self.volume_states))


            elif mutation_type == "regime":

                new_tokens = [t for t in new_tokens if "market" not in t]
                new_tokens.append(random.choice(self.market_regimes))


            elif mutation_type == "session":

                new_tokens = [t for t in new_tokens if "session_" not in t]
                new_tokens.append(random.choice(self.sessions))


            elif mutation_type == "volatility":

                new_tokens = [t for t in new_tokens if "volatility_" not in t]
                new_tokens.append(random.choice(self.volatility_states))


            elif mutation_type == "trend_strength":

                new_tokens = [t for t in new_tokens if t not in self.trend_strength_states]
                new_tokens.append(random.choice(self.trend_strength_states))


            new_tokens = list(set(new_tokens))

            mutations.append(" ".join(sorted(new_tokens)))

        return mutations