# outcome_engine.py

import json
import os


class OutcomeEngine:
    def __init__(self, path="trades.json"):
        self.path = path
        self.trades = []
        self.load()

    def load(self):
        if not os.path.exists(self.path):
            self.trades = []
            return

        try:
            with open(self.path, "r") as f:
                self.trades = json.load(f)
        except:
            self.trades = []

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.trades, f, indent=4)

    def update(self):
        # reload before usage
        self.load()

    def register(self, trade):
        self.trades.append(trade)
        self.save()

    def get_stats(self):
        if not self.trades:
            return {
                "total": 0,
                "wins": 0,
                "losses": 0,
                "winrate": 0,
                "loss_streak": 0
            }

        wins = sum(1 for t in self.trades if t.get("result") == "win")
        losses = sum(1 for t in self.trades if t.get("result") == "loss")

        total = len(self.trades)
        winrate = wins / total if total > 0 else 0

        # loss streak
        loss_streak = 0
        for t in reversed(self.trades):
            if t.get("result") == "loss":
                loss_streak += 1
            else:
                break

        return {
            "total": total,
            "wins": wins,
            "losses": losses,
            "winrate": round(winrate, 2),
            "loss_streak": loss_streak
        }

    def allow_trade(self):
        stats = self.get_stats()

        # 🔥 КЛЮЧОВИЙ ФІКС
        if stats["total"] == 0:
            print("[RISK] No history → allow trading")
            return True

        # 🔥 LIMIT
        LOSS_STREAK_LIMIT = 3

        if stats["loss_streak"] >= LOSS_STREAK_LIMIT:
            print("[RISK] BLOCK: loss streak limit reached")
            return False

        return True