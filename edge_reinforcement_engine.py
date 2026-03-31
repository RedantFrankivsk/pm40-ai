import json


class EdgeReinforcementEngine:

    def __init__(self):

        self.experience_file = "experience_memory.json"

    def load_experience(self):

        with open(self.experience_file, "r") as f:
            return json.load(f)

    def pattern_reinforcement(self):

        data = self.load_experience()

        stats = {}

        for e in data:

            pattern = e["pattern"]

            if pattern not in stats:

                stats[pattern] = {
                    "trades": 0,
                    "wins": 0
                }

            stats[pattern]["trades"] += 1

            if e["result"] == "WIN":

                stats[pattern]["wins"] += 1

        reinforced = []

        for p in stats:

            trades = stats[p]["trades"]
            wins = stats[p]["wins"]

            winrate = wins / trades if trades > 0 else 0

            strength = (winrate - 0.5) * trades

            reinforced.append({
                "pattern": p,
                "trades": trades,
                "wins": wins,
                "winrate": winrate,
                "strength": strength
            })

        reinforced.sort(key=lambda x: x["strength"], reverse=True)

        return reinforced

    def strongest_patterns(self, top=5):

        patterns = self.pattern_reinforcement()

        return patterns[:top]