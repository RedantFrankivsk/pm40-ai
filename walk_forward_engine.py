import random


class WalkForwardEngine:

    def __init__(self):

        self.train_trades = 120
        self.test_trades = 80
        self.forward_trades = 60

    def simulate(self, trades):

        wins = 0

        for _ in range(trades):

            if random.random() < 0.58:
                wins += 1

        return wins / trades

    def run(self):

        train_winrate = self.simulate(self.train_trades)

        test_winrate = self.simulate(self.test_trades)

        forward_winrate = self.simulate(self.forward_trades)

        stability = abs(train_winrate - test_winrate)

        if stability < 0.10 and forward_winrate >= 0.55:
            status = "robust"
        else:
            status = "unstable"

        result = {

            "train_winrate": round(train_winrate, 3),
            "test_winrate": round(test_winrate, 3),
            "forward_winrate": round(forward_winrate, 3),
            "stability": round(stability, 3),
            "status": status
        }

        return result