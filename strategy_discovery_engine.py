import json
import os
from collections import Counter


class StrategyDiscoveryEngine:

    def __init__(self):

        self.pattern_file = "pattern_memory.json"
        self.output_file = "strategy_discovery.json"

    def load_patterns(self):

        if not os.path.exists(self.pattern_file):
            return {}

        with open(self.pattern_file, "r") as f:
            return json.load(f)

    def save(self, strategies):

        with open(self.output_file, "w") as f:
            json.dump(strategies, f, indent=4)

    def extract_features(self, description):

        description = description.lower()

        features = []

        if "up" in description:
            features.append("trend_up")

        if "down" in description:
            features.append("trend_down")

        if "pullback" in description:
            features.append("pullback")

        if "trend" in description:
            features.append("trend_market")

        if "liquidity" in description:
            features.append("liquidity")

        return features

    def run(self):

        patterns = self.load_patterns()

        combo_counter = Counter()

        # 🔥 FIX: працюємо з dict
        for key, stats in patterns.items():

            description = str(key)

            features = self.extract_features(description)

            if len(features) == 0:
                continue

            combo = tuple(sorted(set(features)))

            combo_counter[combo] += stats.get("trades", 1)

        strategies = []

        for combo, count in combo_counter.items():

            trades = count

            winrate = round(0.5 + min(0.01 * count, 0.2), 3)

            strategy = {

                "pattern": " ".join(combo),
                "trades": trades,
                "winrate": winrate,
                "score": round((winrate - 0.5) * trades, 3)

            }

            strategies.append(strategy)

        self.save(strategies)

        return strategies