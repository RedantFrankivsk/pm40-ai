import json
import os
import random


class CuriosityEngine:

    def __init__(self):

        self.pattern_file = "pattern_memory_storage.json"

    def load_patterns(self):

        if not os.path.exists(self.pattern_file):
            return {}

        with open(self.pattern_file, "r") as f:
            return json.load(f)

    def find_rare_patterns(self):

        patterns = self.load_patterns()

        rare = []

        for pattern, data in patterns.items():

            trades = data.get("trades", 0)

            if trades < 3:

                rare.append({

                    "pattern": pattern,
                    "trades": trades
                })

        return rare

    def pick_random(self):

        rare = self.find_rare_patterns()

        if not rare:
            return None

        return random.choice(rare)