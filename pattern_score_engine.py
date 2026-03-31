import math


class PatternScoreEngine:

    def calculate(self, trades, wins):

        if trades == 0:
            return 0

        winrate = wins / trades

        # confidence factor based on trade count
        confidence = math.log(trades + 1)

        # edge over random (0.5 baseline)
        edge = winrate - 0.5

        score = edge * confidence

        return round(score, 4)