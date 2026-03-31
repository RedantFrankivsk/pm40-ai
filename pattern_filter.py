class PatternFilter:

    def __init__(self):
        self.stats = {}

    def allow(self, description):

        if description not in self.stats:
            return True

        trades = self.stats[description]["trades"]
        wins = self.stats[description]["wins"]
        losses = self.stats[description]["losses"]

        total = wins + losses

        if total < 15:
            return True

        winrate = wins / total

        # слабкі патерни блокуємо
        if winrate < 0.45:
            return False

        return True

    def update(self, description, outcome):

        if description not in self.stats:

            self.stats[description] = {
                "trades": 0,
                "wins": 0,
                "losses": 0
            }

        self.stats[description]["trades"] += 1

        if outcome == "WIN":
            self.stats[description]["wins"] += 1

        if outcome == "LOSS":
            self.stats[description]["losses"] += 1